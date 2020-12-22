import pickle
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse,JsonResponse, HttpRequest
from django.core.serializers.json import DjangoJSONEncoder
# youtube imports
import pprint as pp
from googleapiclient.discovery import build
import requests as req
import json
from mediaApp.models import VideoFile
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.oauth2 import id_token
from google.auth.transport import requests
import os
from apiclient.errors import HttpError

# creating a home view
def home(request):
    return render(request,'mediaApp/home.html',)

def glogin(request):
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    with open('./credentials.json') as f:
        data = json.load(f)
    URL = "https://www.googleapis.com/oauth2/v3/userinfo?access_token="+data['access_token']
    r = req.get(url = URL)
    data = r.json()
    print(data['name'])
    context = {
        'glogin':True,
        'name': data['name']
    }
    return render(request,'mediaApp/home.html',context)

def glogout(request):
    os.remove("./credentials.json")
    return render(request,'users/logout.html')

# Get Local Videos apis
def get_videos(query):
    try:
        data =list(VideoFile.objects.filter(title__icontains=query).values())  # wrap in list(), because QuerySet is not JSON serializable
        #return JsonResponse(data, safe=False)  # or JsonResponse({'data': data}
        for q in data:
            q['timestamp']=str(q['timestamp'])
            q['Video_file']=q['Video_file'][9:]
        return data
    except:
        data = json.dumps([{ 'Error': 'No video with that name'}])
        return data  # or JsonResponse({'data': data}

def download(request):
    ikey = request.POST.get('ikey')
    iname = request.POST.get('iname')
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    file6 = drive.CreateFile({'id': ikey})
    file6.GetContentFile(iname)
    context = request.session['context']
    return render(request, 'mediaApp/home.html', context)

def gdrive_process(query):
    if(query == False):
        return {'No Results':'Enter Something in Search Bar'}
    out = {}
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    #Visit : https://developers.google.com/drive/api/v2/search-files for query
    #Visit : https://googleworkspace.github.io/PyDrive/docs/build/html/index.html for Documentation
    file_list = drive.ListFile({'q': "mimeType != 'application/vnd.google-apps.folder' and title contains '"+query+"' "}).GetList()
    for file1 in file_list:
        file1.FetchMetadata()
        if int(file1['fileSize']) < 100*1024*1024:
            print('title: {}, id: {}'.format(file1['title'], file1['id']))
            out[file1['id']]=file1['title']
            if(file1['title'].split('.')[-1]=='mp4'):
                print("Changing Permission")
                file1.InsertPermission({
                            'type': 'anyone',
                            'value': 'anyone',
                            'role': 'reader'})
    return out

def youtube_query(request):
    query = request.POST['query']
    api_key = "AIzaSyBWBwvL9nWDRsriGHZb7FlcQ_9N3T8y27g"
    max_no_of_videos = 5
    error = False
    error_message = None
    try:
        youtube = build('youtube', 'v3', developerKey=api_key)
        youtube_req = youtube.search().list(q=query, part='snippet', type='video', maxResults=max_no_of_videos)
        response = youtube_req.execute()
    except HttpError as err:
        error_code = err.resp.status
        if error_code == 400:
            error_message = "YOUTUBE API KEY INVALID"
        elif error_code == 403:
            error_message = "YOUTUBE API KEY REQUEST QUOTA EXCEEDED"
        else:
            error_message = "SOMETHING WENT WRONG IN YOUTUBE API with ERROR code : " + str(error_code)
        error = True

    videos = []
    if error == False:
        no_of_videos_to_parse = min(max_no_of_videos, len(response['items']))
        for id in range(no_of_videos_to_parse):
            videos.append({
                    'video_id': response['items'][id]['id']['videoId'],
                    'video_title': response['items'][id]['snippet']['title'],
                    'thumbnail': response['items'][id]['snippet']['thumbnails']['default']['url'],
                    'page_link': id,
            })
    url_query = query.replace(" ", "%20")   # for getting all words of query in url (url ignores spaces)

    if os.path.isfile('./credentials.json'):
        with open('./credentials.json') as f:
            data = json.load(f)
        URL = "https://www.googleapis.com/oauth2/v3/userinfo?access_token="+data['access_token']
        r = req.get(url = URL)
        data = r.json()
        print(data['name'])
        out = gdrive_process(query)
        context = {
                'videos': videos,
                'show_more_link': "https://www.youtube.com/results?search_query="+url_query,
                'original_query': query,
                'query_processed': True,
                'glogin': True,
                'name': data['name'],
                'out' : out
        }
    else:
        context = {
                'videos': videos,
                'show_more_link': "https://www.youtube.com/results?search_query="+url_query,
                'original_query': query,
                'query_processed': True,
        }
    context['youtube_error_status'] = error
    context['youtube_error_message'] = error_message
    print(error)
    print(error_message)
    context['api_response']=get_videos(query)
    request.session['context'] = context
    return render(request, 'mediaApp/home.html', context)
    #return JsonResponse(context)

def show_video(request, vid=None):
    vid = int(vid)
    context = request.session['context']
    context['current_video_id'] = "https://www.youtube.com/embed/" + context['videos'][vid]['video_id']
    return render(request, 'mediaApp/home.html', context)

def show_local_video(request, vid=None):
    context = request.session['context']
    context['current_api_video_id'] = vid
    return render(request, 'mediaApp/home.html', context)

def show_drive_video(request, vid=None):
    context = request.session['context']
    context['flag'] = False
    url = "https://www.googleapis.com/drive/v3/files/"+vid+"?alt=media&key=AIzaSyDBIemLvDdcof-qTcpGjPys48ahu_xxt-s"
    print("!!",vid)
    flag = True
    context['current_drive_id'] = vid
    context['flag'] = True
    return render(request, 'mediaApp/home.html', context)

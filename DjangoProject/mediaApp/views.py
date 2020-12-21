import pickle
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# youtube imports
import pprint as pp
from googleapiclient.discovery import build



# creating a home view
def home(request):
    return render(request,'mediaApp/home.html',)


def youtube_query(request):
    query = request.POST['query']
    api_key = "AIzaSyAjvu_NH7dUsxBk0xuj4ropBwfFohr6l5Y"
    youtube = build('youtube', 'v3', developerKey=api_key)
    max_no_of_videos = 5
    youtube_req = youtube.search().list(q=query, part='snippet', type='video', maxResults=max_no_of_videos)
    response = youtube_req.execute()
    videos = []
    for id in range(min(max_no_of_videos, len(response['items']))):
        videos.append({
                'video_id': response['items'][id]['id']['videoId'],
                'video_title': response['items'][id]['snippet']['title'],
                'thumbnail': response['items'][id]['snippet']['thumbnails']['default']['url'],
                'page_link': id,
        })

    # context = {'videoId' : "https://www.youtube.com/embed/" + str(videoId)}
    context = {
            'videos': videos,
            'show_more_link': "https://www.youtube.com/results?search_query="+query,
            'original_query': query,
            'query_processed': True
    }
    request.session['context'] = context
    return render(request, 'mediaApp/home.html', context)


def show_video(request, vid=None):
    vid = int(vid)
    context = request.session['context']
    context['current_video_id'] = "https://www.youtube.com/embed/" + context['videos'][vid]['video_id']
    return render(request, 'mediaApp/home.html', context)





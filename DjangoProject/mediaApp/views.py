import pickle
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse,JsonResponse
# youtube imports
import pprint as pp
from googleapiclient.discovery import build

import json
from mediaApp.models import VideoFile


# creating a home view
def home(request):
    return render(request,'mediaApp/home.html',)

# Get Local Videos apis
def get_videos(request):
    if request.method == 'GET':
        try:
            data = list(VideoFile.objects.values())  # wrap in list(), because QuerySet is not JSON serializable
            return JsonResponse(data, safe=False)  # or JsonResponse({'data': data})
        except:
            data = json.dumps([{ 'Error': 'No video with that name'}])
            return JsonResponse(data, safe=False)  # or JsonResponse({'data': data}

def youtube_query(request, query=None):

    query = request.POST['query'] 
    print(request.POST, '='*20, query)

    api_key = 'AIzaSyAjvu_NH7dUsxBk0xuj4ropBwfFohr6l5Y'
    youtube = build('youtube', 'v3', developerKey=api_key)

    r = youtube.search().list(q=query, part='snippet', type='video', maxResults=1)

    response = r.execute()

    videoId = response['items'][0]['id']['videoId'] # returns single videoId
    context = {'videoId' : "https://www.youtube.com/embed/" + str(videoId)}
    return render(request,'mediaApp/home.html', context)

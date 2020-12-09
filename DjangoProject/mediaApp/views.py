import pickle
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# youtube imports
import pprint as pp
from googleapiclient.discovery import build



# creating a home view
def home(request):
    return render(request,'mediaApp/home.html',)


def youtube_query(request, query=None):

    query = request.POST['query'] 
    print(request.POST, '='*20, query)

    api_key = 'AIzaSyAjvu_NH7dUsxBk0xuj4ropBwfFohr6l5Y'
    youtube = build('youtube', 'v3', developerKey=api_key)

    r = youtube.search().list(q=query, part='snippet', type='video', maxResults=1)

    response = r.execute()

    videoId = response['items'][0]['id']['videoid'] # returns single videoId
    # for record in response['items'] :
        # print(record['id']['videoId'])
    # return 
    render(request,'mediaApp/home.html', {'videoId' : videoId})

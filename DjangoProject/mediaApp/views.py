import pickle
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# youtube imports
import pprint as pp
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


# creating a home view
def home(request):
    return render(request,'mediaApp/home.html',)


def youtube_query(request, query):
    credentials = None

    # token.pickle stores the user's credentials from previously successful logins
    if os.path.exists('token.pickle'):
        print('Loading Credentials From File...')
        with open('token.pickle', 'rb') as token:
            credentials = pickle.load(token)

    # If there are no valid credentials available, then either refresh the token or log in.
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            print('Refreshing Access Token...')
            credentials.refresh(Request())
        else:
            print('Fetching New Tokens...')
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secrets.json',
                scopes=[
                    # 'https://www.googleapis.com/auth/youtube.readonly',
                    'https://www.googleapis.com/auth/youtube.force-ssl'
                ]
            )

            flow.run_local_server(port=8080, prompt='consent',
                                  authorization_prompt_message='')
            credentials = flow.credentials

            # Save the credentials for the next run
            with open('token.pickle', 'wb') as f:
                print('Saving Credentials for Future Use...')
                pickle.dump(credentials, f)

    youtube = build('youtube', 'v3', credentials=credentials)


    request = youtube.search().list(q=query, part='snippet', type='video', maxResults=1)

    response = request.execute()
    # pp.pprint(response)
    videoId = response['items'][0]['id']['videoid'] # returns single videoId
    # for record in response['items'] :
        # print(record['id']['videoId'])

    return {'videoId' : videoId}

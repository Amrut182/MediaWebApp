from __future__ import print_function
from django.shortcuts import render,redirect
from django.http import HttpResponse
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def home(request):
    #query = request.POST['query']
    query = request.POST.get('query', False)
    out = process(query)
    return render(request,'home.html',{'out':out})

def process(query):
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
        print('title: {}, id: {}'.format(file1['title'], file1['id']))
        out[file1['id']]=file1['title']
        if(file1['title'].split('.')[-1]=='mp4'):
            print("Changing Permission")
            file1.InsertPermission({
                        'type': 'anyone',
                        'value': 'anyone',
                        'role': 'reader'})
    return out

def download(request):
    ikey = request.POST.get('ikey')
    iname = request.POST.get('iname')
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    file6 = drive.CreateFile({'id': ikey})
    file6.GetContentFile(iname)
    return redirect('Home')
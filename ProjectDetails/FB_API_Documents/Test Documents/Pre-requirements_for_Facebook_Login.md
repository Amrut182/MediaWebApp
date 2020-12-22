Pre-requirements:
For permission granting we have used third party app, developed officially by developers.facebook.com., So yo have to create account on them and setup the permissions for that you just have to follow the steps:
1. Visit https://developers.facebook.com/apps
2. You have to create your personal app then, follow the steps:
    a. You have an option for creating new app. Click on that.
    b. Select Build Connected Experiences. Continue
    c. Add Display app name, and create it.
    d. Now go to Settings -> Basic at bottom. First click on the button + Add Platform and add a website. For the Site URL put http://localhost:8000 and then in the App Domains put just localhost
    e. Copy that App ID and App secret then paste that IDs in DjangoProject/mediaWebApp/settings.py  at bottom SOCIAL_AUTH_FACEBOOK_KEY = 'Paste_App_ID_here'  # App ID, SOCIAL_AUTH_FACEBOOK_SECRET = 'Paste_secret_ID_here'  # App Secret
3. Now you can run your site.

Note: For tesing purpose we can provide you our private id in which we have already setup this settings. 

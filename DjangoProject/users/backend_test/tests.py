from django.test import TestCase, Client        
from users.forms import UserLoginForm
from users.views import signup
import unittest 

class backend_test(TestCase,unittest.TestCase):

    # Signup form (unit testing)
    def test_signup_form(self):
        #1 email is blank
        form = UserLoginForm(data={'username':"abcdef",
                            'email': "",
                            'password1': "Abc@abcd",
                            'password2': "Abc@abcd"})
        self.assertFalse(form.is_valid())

        #2 email is not valid
        form = UserLoginForm(data={'username':"abcdef",
                            'email': "abc.xyz.com",
                            'password1': "Abc@abcd",
                            'password2': "Abc@abcd"})
        self.assertFalse(form.is_valid())

        #3 username is blank
        form = UserLoginForm(data={'username':"",
                            'email': "abc@xyz.com",
                            'password1': "Abc@abcd",
                            'password2': "Abc@abcd"})
        self.assertFalse(form.is_valid())

        #4 username is not valid
        form = UserLoginForm(data={'username':"user name",
                            'email': "abc@xyz.com",
                            'password1': "Abc@abcd",
                            'password2': "Abc@abcd"})
        self.assertFalse(form.is_valid())

        #5 passwords are not matching
        form = UserLoginForm(data={'username':"abcdef",
                            'email': "abc@gmail.com",
                            'password1': "Abc@ab",
                            'password2': "pass"})
        self.assertFalse(form.is_valid())

        #6 password is blank (not matching) & username is not correct
        form = UserLoginForm(data={'username':"John Culen",
                            'email': "abc@gmail.com",
                            'password1': "Abc@ab",
                            'password2': ""})
        self.assertFalse(form.is_valid())

        #7 password size is smaller than 8 & username is not correct
        form = UserLoginForm(data={'username':"John@Culen",
                            'email': "abc@gmail.in.com",
                            'password1': "test",
                            'password2': "test"})
        self.assertFalse(form.is_valid())

        #8 password is too similar to username
        form = UserLoginForm(data={'username':"JohnCulen",
                            'email': "abc@gmail.in.com",
                            'password1': "JohnCulen",
                            'password2': "JohnCulen"})
        self.assertFalse(form.is_valid())

        #9 multiple errors
        form = UserLoginForm(data={'username':"John Culen",
                            'email': "abc.gmail.in.com",
                            'password1': "John Culen",
                            'password2': "John"})
        self.assertFalse(form.is_valid())

        #10/11 to make a valid acount and check if another account can be made using same username
        # multiple errors
        form = UserLoginForm(data={'username':"JohnCulen",
                            'email': "abc@gmail.com",
                            'password1': "iawueawe",
                            'password2': "iawueawe"})
        self.assertTrue(form.is_valid())
        form.save() 
        form = UserLoginForm(data={'username':"JohnCulen",
                            'email': "abc@gmail.com",
                            'password1': "asdfasdf",
                            'password2': "asdfasdf"})
        self.assertFalse(form.is_valid())
    
    # Signup View (integration testing)
    def test_signup_view(self):
        c = Client()

        #1 email is blank
        response = c.post('/signup/',{'username':"abcdef",
                            'email': "",
                            'password1': "Abc@abcd",
                            'password2': "Abc@abcd"})
        self.assertIsNotNone(response.context)

        #2 email is not valid
        response = c.post('/signup/',{'username':"abcdef",
                            'email': "abc.xyz.com",
                            'password1': "Abc@abcd",
                            'password2': "Abc@abcd"})
        self.assertIsNotNone(response.context)

        #3 username is blank
        response = c.post('/signup/',{'username':"",
                            'email': "abc@xyz.com",
                            'password1': "Abc@abcd",
                            'password2': "Abc@abcd"})
        self.assertIsNotNone(response.context)

        #4 username is not valid
        response = c.post('/signup/',{'username':"user name",
                            'email': "abc@xyz.com",
                            'password1': "Abc@abcd",
                            'password2': "Abc@abcd"})
        self.assertIsNotNone(response.context)

        #5 passwords are not matching
        response = c.post('/signup/',{'username':"abcdef",
                            'email': "abc@gmail.com",
                            'password1': "Abc@ab",
                            'password2': "pass"})
        self.assertIsNotNone(response.context)

        #6 password is blank (not matching) & username is not correct
        response = c.post('/signup/',{'username':"John Culen",
                            'email': "abc@gmail.com",
                            'password1': "Abc@ab",
                            'password2': ""})
        self.assertIsNotNone(response.context)

        #7 password size is smaller than 8 & username is not correct
        response = c.post('/signup/',{'username':"John@Culen",
                            'email': "abc@gmail.in.com",
                            'password1': "test",
                            'password2': "test"})
        self.assertIsNotNone(response.context)

        #8 password is too similar to username
        response = c.post('/signup/',{'username':"JohnCulen",
                            'email': "abc@gmail.in.com",
                            'password1': "JohnCulen",
                            'password2': "JohnCulen"})
        self.assertIsNotNone(response.context)

        #9 multiple errors
        response = c.post('/signup/',{'username':"John Culen",
                            'email': "abc.gmail.in.com",
                            'password1': "John Culen",
                            'password2': "John"})
        self.assertIsNotNone(response.context)

        #10/11 to make a valid acount and check if another account can be made using same username
        # multiple errors
        response = c.post('/signup/',{'username':"JohnMcLane",
                            'email': "abc@gmail.com",
                            'password1': "iawueawe",
                            'password2': "iawueawe"})
        self.assertIsNone(response.context)
        response = c.post('/signup/',{'username':"JohnMcLane",
                            'email': "abc@gmail.com",
                            'password1': "asdfasdf",
                            'password2': "asdfasdf"})
        self.assertIsNotNone(response.context)

    # testing for login view(integration)
    def test_login_view(self):
        c = Client()
        # making a user for testing
        form = UserLoginForm(data={'username':"JohnBravo",
                            'email': "abc@gmail.com",
                            'password1': "test@123",
                            'password2': "test@123"})
        self.assertTrue(form.is_valid())
        form.save() 
        
        #1 username is blank
        response = c.post('/login/',{'username':"",
                            'password': "Abc@abcd"})
        self.assertIsNotNone(response.context)

        #2 password is blank
        response = c.post('/login/',{'username':"JohnBravo",
                            'password': ""})
        self.assertIsNotNone(response.context)

        #3 username is wrong
        response = c.post('/login/',{'username':"JohnyBravo",
                            'password': "test@123"})
        self.assertIsNotNone(response.context)

        #4 passwrod is wrong
        response = c.post('/login/',{'username':"JohnBravo",
                            'password': "testing@123"})
        self.assertIsNotNone(response.context)

        #5 correct login
        response = c.post('/login/',{'username':"JohnBravo",
                            'password': "test@123"})
        self.assertEquals(response.url,'/')
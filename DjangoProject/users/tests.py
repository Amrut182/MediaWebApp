from django.test import TestCase, Client        
from .forms import UserLoginForm
from .views import signup

class backend_test(TestCase):

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
    
    # Signup View (?? testing)
    def test_signup_view(self):
        #12 email is blank
        c = Client()
        response = c.post('/signup/', {'username':"JohnCulen",
                            'email': "abc@gmail.com",
                            'password1': "asdfasdf",
                            'password2': "asdfasdf"})
        self.assertEqual(response.status_code,200)
        # form = UserLoginForm(data={'username':"JohnCulen",
        #                     'email': "abc@gmail.com",
        #                     'password1': "asdfasdf",
        #                     'password2': "asdfasdf"},)
        
        # user_signup = signup(form)
        # self.assertFalse(user_signup)

        # #email is not valid
        # form = UserLoginForm(data={'username':"abcdef",
        #                     'email': "abc.xyz.com",
        #                     'password1': "Abc@abcd",
        #                     'password2': "Abc@abcd"})
        # self.assertFalse(form.is_valid())

        # #username is blank
        # form = UserLoginForm(data={'username':"",
        #                     'email': "abc@xyz.com",
        #                     'password1': "Abc@abcd",
        #                     'password2': "Abc@abcd"})
        # self.assertFalse(form.is_valid())

        # #username is not valid
        # form = UserLoginForm(data={'username':"user name",
        #                     'email': "abc@xyz.com",
        #                     'password1': "Abc@abcd",
        #                     'password2': "Abc@abcd"})
        # self.assertFalse(form.is_valid())

        # # passwords are not matching
        # form = UserLoginForm(data={'username':"abcdef",
        #                     'email': "abc@gmail.com",
        #                     'password1': "Abc@ab",
        #                     'password2': "pass"})
        # self.assertFalse(form.is_valid())

        # # password is blank (not matching) & username is not correct
        # form = UserLoginForm(data={'username':"John Culen",
        #                     'email': "abc@gmail.com",
        #                     'password1': "Abc@ab",
        #                     'password2': ""})
        # self.assertFalse(form.is_valid())

        # # password size is smaller than 8 & username is not correct
        # form = UserLoginForm(data={'username':"John@Culen",
        #                     'email': "abc@gmail.in.com",
        #                     'password1': "test",
        #                     'password2': "test"})
        # self.assertFalse(form.is_valid())

        # # password is too similar to username
        # form = UserLoginForm(data={'username':"JohnCulen",
        #                     'email': "abc@gmail.in.com",
        #                     'password1': "JohnCulen",
        #                     'password2': "JohnCulen"})
        # self.assertFalse(form.is_valid())

        # # multiple errors
        # form = UserLoginForm(data={'username':"John Culen",
        #                     'email': "abc.gmail.in.com",
        #                     'password1': "John Culen",
        #                     'password2': "John"})
        # self.assertFalse(form.is_valid())

        # #to make a valid acount and check if another account can be made using same username
        # # multiple errors
        # form = UserLoginForm(data={'username':"JohnCulen",
        #                     'email': "abc@gmail.com",
        #                     'password1': "iawueawe",
        #                     'password2': "iawueawe"})
        # self.assertTrue(form.is_valid())
        # form.save() 
        # form = UserLoginForm(data={'username':"JohnCulen",
        #                     'email': "abc@gmail.com",
        #                     'password1': "asdfasdf",
        #                     'password2': "asdfasdf"})
        # self.assertFalse(form.is_valid())
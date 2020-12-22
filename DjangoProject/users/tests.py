from django.test import TestCase
from .forms import UserLoginForm

class backend_test(TestCase):

    # Signup
    def test_signup_form(self):
        #email is blank
        form = UserLoginForm(data={'username':"abcdef",
                            'email': "",
                            'password1': "Abc@abcd",
                            'password2': "Abc@abcd"})
        self.assertFalse(form.is_valid())

        #email is not valid
        form = UserLoginForm(data={'username':"abcdef",
                            'email': "abc.xyz.com",
                            'password1': "Abc@abcd",
                            'password2': "Abc@abcd"})
        self.assertFalse(form.is_valid())

        #username is blank
        form = UserLoginForm(data={'username':"",
                            'email': "abc@xyz.com",
                            'password1': "Abc@abcd",
                            'password2': "Abc@abcd"})
        self.assertFalse(form.is_valid())

        #username is not valid
        form = UserLoginForm(data={'username':"user name",
                            'email': "abc@xyz.com",
                            'password1': "Abc@abcd",
                            'password2': "Abc@abcd"})
        self.assertFalse(form.is_valid())

        # passwords are not matching
        form = UserLoginForm(data={'username':"abcdef",
                            'email': "abc@gmail.com",
                            'password1': "Abc@ab",
                            'password2': "pass"})
        self.assertFalse(form.is_valid())

        # password is blank (not matching) & username is not correct
        form = UserLoginForm(data={'username':"John Culen",
                            'email': "abc@gmail.com",
                            'password1': "Abc@ab",
                            'password2': ""})
        self.assertFalse(form.is_valid())

        # password size is smaller than 8 & username is not correct
        form = UserLoginForm(data={'username':"John@Culen",
                            'email': "abc@gmail.in.com",
                            'password1': "test",
                            'password2': "test"})
        self.assertFalse(form.is_valid())

        # password is too similar to username
        form = UserLoginForm(data={'username':"JohnCulen",
                            'email': "abc@gmail.in.com",
                            'password1': "JohnCulen",
                            'password2': "JohnCulen"})
        self.assertFalse(form.is_valid())

        # multiple errors
        form = UserLoginForm(data={'username':"John Culen",
                            'email': "abc.gmail.in.com",
                            'password1': "John Culen",
                            'password2': "John"})
        self.assertFalse(form.is_valid())
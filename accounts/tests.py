# Create your tests here.

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class UserAuthenticationViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
    
    def test_signup_page_get(self):
        response = self.client.get(reverse('sign-up'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/sign-up.html')

    def test_signup_page_post(self):
        response = self.client.post(reverse('sign-up'), {
            'username': 'newuser',
            'password1': 'testpassword',
            'password2': 'testpassword'
        })
        self.assertEqual(response.status_code, 200)
        

    def test_signup_page_post_invalid(self):
        response = self.client.post(reverse('sign-up'), {
            'username': 'newuser',
            'password1': 'testpassword',
            'password2': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/sign-up.html')
        self.assertFalse(User.objects.filter(username='newuser').exists())

    def test_signin_page_get(self):
        response = self.client.get(reverse('sign-in'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/sign-in.html')

    def test_signin_page_post(self):
        response = self.client.post(reverse('sign-in'), {
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful sign-in

    def test_signin_page_post_invalid(self):
        response = self.client.post(reverse('sign-in'), {
            'username': 'testuser',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/sign-in.html')

    def test_signout_page(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('sign-out'))
        self.assertEqual(response.status_code, 302)  # Redirect after sign-out
        self.assertRedirects(response, reverse('home'))

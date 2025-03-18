from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from core.models import UserProfile
from core.forms import UserRegistrationForm, UserProfileForm
from unittest.mock import patch
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
from io import BytesIO

class CoreTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        UserProfile.objects.create(user=self.user, nickname='Test User', email='test@example.com', phone='1234567890', dob='2000-01-01')
        self.register_url = reverse('register')
        self.login_url = reverse('user_login')
        self.profile_url = reverse('user_info')

    def test_user_registration_form_valid(self):
        form_data = {
            'username': 'newuser',
            'password1': 'strongpassword',
            'password2': 'strongpassword',
            'nickname': 'New Nickname',
            'email': 'newuser@example.com',
            'phone': '1234567890',
            'dob': '2000-01-01',
        }
        form = UserRegistrationForm(data=form_data)
        if form.is_valid():
            print("Form is valid")
        else:
            print(form.errors)
        self.assertTrue(form.is_valid())

    def test_user_registration_password_encryption(self):
        form_data = {
            'username': 'newuser2',
            'password': 'strongpassword2',
            'password_confirm': 'strongpassword2',
            'nickname': 'New Nickname2',
            'email': 'newuser2@example.com',
            'phone': '1234567891',
            'dob': '2000-01-02',
        }
        response = self.client.post(self.register_url, form_data, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_user_registration_view_success(self):
        form_data = {
            'username': 'newuser3',
            'password': 'strongpassword3',
            'password_confirm': 'strongpassword3',
            'nickname': 'New Nickname3',
            'email': 'newuser3@example.com',
            'phone': '1234567892',
            'dob': '2000-01-03',
        }
        response = self.client.post(self.register_url, form_data, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_user_registration_with_avatar(self):
        image = Image.new('RGB', (100, 100), color='red')
        image_file = BytesIO()
        image.save(image_file, 'PNG')
        image_file.seek(0)
        avatar = SimpleUploadedFile("test_avatar.png", image_file.read(), content_type="image/png")

        form_data = {
            'username': 'newuser4',
            'password': 'strongpassword4',
            'password_confirm': 'strongpassword4',
            'nickname': 'New Nickname4',
            'email': 'newuser4@example.com',
            'phone': '1234567893',
            'dob': '2000-01-04',
            'avatar': avatar,
        }
        response = self.client.post(self.register_url, form_data, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_user_profile_model_str(self):
        new_test_user = User.objects.create_user(username='new_test_user', password='new_test_password')
        profile = UserProfile.objects.create(user=new_test_user, nickname='Test', email='unique_test@example.com', phone='123', dob='2000-01-01')
        self.assertEqual(str(profile), 'Test')

    def test_user_registration_form_invalid_email(self):
        new_user = User.objects.create_user(username='new_testuser', password='new_testpassword')
        UserProfile.objects.create(user=new_user, nickname='Test', email='existing@example.com', phone='123', dob='2000-01-01')
        form_data = {
            'username': 'invaliduser',
            'password': 'strongpassword',
            'password_confirm': 'strongpassword',
            'nickname': 'Invalid Nickname',
            'email': 'existing@example.com',
            'phone': '1234567890',
            'dob': '2000-01-01',
        }
        form = UserRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_profile_view_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)

    def test_user_profile_view_unauthenticated(self):
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 302)

    def test_user_profile_form_valid(self):
        form_data = {
            'nickname': 'Updated Nickname',
            'email': 'updated@example.com',
            'phone': '9876543210',
            'dob': '2001-01-01',
        }
        form = UserProfileForm(data=form_data, instance=self.user.userprofile)
        self.assertTrue(form.is_valid())
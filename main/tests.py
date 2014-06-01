# -*- encoding: utf-8 -*-

from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client

from .models import Photo
from .views import hello_name

class MainTestCase(TestCase):
    def setUp(self):
    	user = User.objects.create_user('tyrion', 'tyrion@kingslanding.gov', 'shae')
        Photo.objects.create(user=user, title=u'Photo without image', published=False)

    def test_empty_photos_list(self):
    	"""Sprawdzenie czy zdjęcia z publisjed=False nie są pokazywane"""
    	client = Client()
    	response = client.get('/')
    	self.assertEqual(response.content.find('<article>'), -1)


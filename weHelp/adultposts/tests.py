from django.test import TestCase
from django.test import SimpleTestCase
from django.test import RequestFactory, TestCase
from django.contrib.auth.models import AnonymousUser, User
from adultposts.views import *
from adultposts.models import *
from adultposts.forms import *


class postcreate(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_post_create(self):
        request = self.factory.get('post_create')
        request.user = AnonymousUser()
        response = post_create(request)
        self.assertEqual(response.status_code, 302)
        self.assertNotEqual(response.status_code, 404)
# Create your tests here.

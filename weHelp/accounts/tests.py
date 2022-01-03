from django.test import TestCase
from django.test import SimpleTestCase
from django.test import RequestFactory, TestCase
from django.contrib.auth.models import AnonymousUser, User
from accounts.views import *
from accounts.models import *
from accounts.forms import *


class sign(SimpleTestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_signup_view(self):
        request = self.factory.get('signup_view')
        response = signup_view(request)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 404)

    def test_login_view(self):
        request = self.factory.get('login_view')
        response = login_view(request)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 404)


class adultlogin(SimpleTestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_adult_login(self):
        request = self.factory.get('adult_login')
        response = adult_login(request)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 404)


class younglogin(SimpleTestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_young_login(self):
        request = self.factory.get('young_login')
        response = young_login(request)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 404)


class younghompage(SimpleTestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_young_hompage(self):
        request = self.factory.get('young_hompage')
        request.user = AnonymousUser()
        response = young_hompage(request)
        self.assertEqual(response.status_code, 302)
        self.assertNotEqual(response.status_code, 404)


class youngsavedposts(SimpleTestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_young_saved_posts(self):
        request = self.factory.get('young_saved_posts')
        request.user = AnonymousUser()
        response = young_saved_posts(request)
        self.assertEqual(response.status_code, 302)
        self.assertNotEqual(response.status_code, 404)


class adminhomepage(SimpleTestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_admin_homepage(self):
        request = self.factory.get('admin_homepage')
        request.user = AnonymousUser()
        response = admin_homepage(request)
        self.assertEqual(response.status_code, 302)
        self.assertNotEqual(response.status_code, 404)


class adminadult(SimpleTestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_admin_adult(self):
        request = self.factory.get('admin_adult')
        request.user = AnonymousUser()
        response = admin_adult(request)
        self.assertEqual(response.status_code, 302)
        self.assertNotEqual(response.status_code, 404)


class adminyoung(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_admin_young(self):
        request = self.factory.get('admin_young')
        request.user = AnonymousUser()
        response = admin_young(request)
        self.assertEqual(response.status_code, 302)
        self.assertNotEqual(response.status_code, 404)


class adminposts(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_admin_posts(self):
        request = self.factory.get('admin_posts')
        request.user = AnonymousUser()
        response = admin_posts(request)
        self.assertEqual(response.status_code, 302)
        self.assertNotEqual(response.status_code, 404)
# Create your tests here.

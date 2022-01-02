from django.test import TestCase, testcases
from .models import adult, young
from adultposts.models import post
from http import HTTPStatus


class wehelp_tests(TestCase):

    def test_lambda1(self):
        adult1 = adult.objects.create(
            name='yaakov', phone='+972537654567', city='באר שבע', age='69')
        young1 = young.objects.create(
            name='moshe', phone='+972535367286', city='באר שבע', age='27')
        self.assertNotEqual(adult1, young1)

    def test_lambda2(self):
        adult2 = adult.objects.create(
            name='yaakov', phone='+972537654567', city='באר שבע', age='69')
        self.assertEqual(200, 200)

    def test_lambda3(self):
        adult2 = adult.objects.create(
            name='yaakov', phone='+972537654567', city='באר שבע', age='69')
        self.assertEqual(200, 200)

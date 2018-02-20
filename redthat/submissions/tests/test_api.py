from unittest import mock

from django.conf import settings

from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token

from model_mommy import mommy

from ..models import Submission


class SubmissionsAPITestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()

        self.submission1 = mommy.make(Submission)

    def test_submission_detail(self):
        """
        Test that we can return the details of a self.submission1
        """
        response = self.client.get(f'/submissions/{self.submission1.id}/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {
            'url': 'http://testserver/submissions/1/',
            'title': self.submission1.title,
            'external_link': self.submission1.external_link,
            'upvotes': 0,
            'downvotes': 0
        })

    def test_submission_list(self):
        """
        Test that we can return a list of Submissions
        """
        response = self.client.get('/submissions/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {
            'count': 1,
            'next': None,
            'previous': None,
            'results': [
                {
                    'url': 'http://testserver/submissions/1/',
                    'title': self.submission1.title,
                    'external_link': self.submission1.external_link,
                    'upvotes': 0,
                    'downvotes': 0
                }
            ]
        })

    def test_unauthenticated(self):
        """
        Test all unauthenticated interactions with the Submissions endpoint
        """
        list_endpoint = '/submissions/'
        detail_endpoint = '/submissions/1/'

        self.assertEqual(self.client.get(list_endpoint).status_code, 200)
        self.assertEqual(self.client.post(list_endpoint).status_code, 401)
        self.assertEqual(self.client.put(list_endpoint).status_code, 401)
        self.assertEqual(self.client.patch(list_endpoint).status_code, 401)
        self.assertEqual(self.client.delete(list_endpoint).status_code, 401)
        self.assertEqual(self.client.head(list_endpoint).status_code, 200)
        self.assertEqual(self.client.options(list_endpoint).status_code, 200)

        self.assertEqual(self.client.get(detail_endpoint).status_code, 200)
        self.assertEqual(self.client.post(detail_endpoint).status_code, 401)
        self.assertEqual(self.client.put(detail_endpoint).status_code, 401)
        self.assertEqual(self.client.patch(detail_endpoint).status_code, 401)
        self.assertEqual(self.client.delete(detail_endpoint).status_code, 401)
        self.assertEqual(self.client.head(detail_endpoint).status_code, 200)
        self.assertEqual(self.client.options(detail_endpoint).status_code, 200)

    @mock.patch('requests.get')
    def test_authenticated(self, mock_get):
        """
        Test all authenticated interactions with the Submissions endpoint
        """
        mock_get.return_value.content = '<title>Moby Dick</title>'
        list_endpoint = '/submissions/'
        detail_endpoint = '/submissions/1/'
        token = mommy.make(Token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')

        self.assertEqual(self.client.get(list_endpoint).status_code, 200)
        self.assertEqual(self.client.post(list_endpoint, {
            'external_link': 'http://example.com/logged/in/'
        }).status_code, 201)
        self.assertEqual(self.client.put(list_endpoint).status_code, 405)
        self.assertEqual(self.client.patch(list_endpoint).status_code, 405)
        self.assertEqual(self.client.delete(list_endpoint).status_code, 405)
        self.assertEqual(self.client.head(list_endpoint).status_code, 200)
        self.assertEqual(self.client.options(list_endpoint).status_code, 200)

        self.assertEqual(self.client.get(detail_endpoint).status_code, 200)
        self.assertEqual(self.client.post(detail_endpoint).status_code, 405)
        self.assertEqual(self.client.put(detail_endpoint).status_code, 405)
        self.assertEqual(self.client.patch(detail_endpoint).status_code, 405)
        self.assertEqual(self.client.delete(detail_endpoint).status_code, 405)
        self.assertEqual(self.client.head(detail_endpoint).status_code, 200)
        self.assertEqual(self.client.options(detail_endpoint).status_code, 200)

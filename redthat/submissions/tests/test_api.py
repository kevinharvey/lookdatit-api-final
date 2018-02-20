from rest_framework.test import APITestCase, APIClient

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

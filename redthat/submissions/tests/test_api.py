from rest_framework.test import APITestCase, APIClient

from model_mommy import mommy

from ..models import Submission


class SubmissionsAPITestCase(APITestCase):

    def test_unauthenticated(self):
        """
        Test that an unauthenticated user can access the submissions endpoints
        """
        client = APIClient()
        submission = mommy.make(Submission)

        response = client.get(f'/submissions/{submission.id}/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['url'],
            'http://testserver/submissions/1/')
        self.assertEqual(response.data['title'], submission.title)
        self.assertEqual(response.data['external_link'],
            submission.external_link)
        self.assertEqual(response.data['upvotes'], 0)
        self.assertEqual(response.data['downvotes'], 0)

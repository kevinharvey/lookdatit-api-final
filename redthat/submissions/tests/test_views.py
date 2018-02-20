from unittest import mock

from rest_framework.test import APITestCase

from ..views import SubmissionSerializer
from ..models import Submission


class SubmissionSerializerTestCase(APITestCase):

    @mock.patch('requests.get')
    def test_create(self, mock_get):
        """
        Test that we get the title from the document hosted at the external_link
        """
        mock_get.return_value.content = '<html><title>Title of Thing</title></html>'
        
        serializer = SubmissionSerializer(data={
            'external_link': 'http://example.com/title-of-thing/'
        })
        serializer.is_valid()
        serializer.save()

        submission = Submission.objects.first()
        self.assertEqual(submission.title, 'Title of Thing')

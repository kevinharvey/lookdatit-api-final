from rest_framework import serializers, viewsets, mixins

import requests
from bs4 import BeautifulSoup

from .models import Submission


class SubmissionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Submission
        fields = (
            'url', 'title', 'external_link', 'upvotes', 'downvotes',
        )
        read_only_fields = (
            'title',
        )

    def create(self, validated_data):
        """
        Get the external_link and grab the title
        """
        response = requests.get(validated_data['external_link'])
        soup = BeautifulSoup(response.content, 'html.parser')
        validated_data['title'] = soup.title.string

        return super().create(validated_data)


class SubmissionViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
    mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer

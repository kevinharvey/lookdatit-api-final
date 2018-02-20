from rest_framework import serializers, viewsets, mixins

from .models import Submission


class SubmissionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Submission
        fields = (
            'url', 'title', 'external_link', 'upvotes', 'downvotes',
        )


class SubmissionViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer

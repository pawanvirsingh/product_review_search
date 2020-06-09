from rest_framework import serializers
from review_management import models


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        exclude = ('helpfulness_score',)

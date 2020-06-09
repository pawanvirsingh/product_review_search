from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet
from review_management.api.serializers import ReviewSerializer
from review_management.models import Review


class ReviewViewSet(ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = ReviewSerializer

    def get_queryset(self):
        keyword = self.request.GET.get('query', None)
        if keyword:
            return Review.objects.filter(text__icontains=keyword).order_by("-helpfulness_score", "-score")
        return []

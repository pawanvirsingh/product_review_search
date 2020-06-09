from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from product_review_search.users.api.views import UserViewSet
from product_review_search.review_management.api.views import ReviewViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register('review-search', ReviewViewSet, basename="review")



app_name = "api"
urlpatterns = router.urls

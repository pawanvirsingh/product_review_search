from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "product_review_search.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import product_review_search.users.signals  # noqa F401
        except ImportError:
            pass

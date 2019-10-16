from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.utils.translation import gettext_lazy as _


class BaseConfig(AppConfig):
    name = 'client.base'
    verbose_name = _("Modulo deL Sistema")
    verbose_name_plural = _("Modulo deL Sistema")
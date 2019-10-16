from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.utils.translation import gettext_lazy as _


class UserConfig(AppConfig):
    name = 'server.auth'
    label = 'profile'
    verbose_name = _("Modulo de Usuario")
    verbose_name_plural = _("Modulo de Usuarios")
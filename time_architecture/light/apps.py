from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class LightConfig(AppConfig):
    name = 'time_architecture.light'
    label = 'light'
    verbose_name = _('Light control')
    verbose_name_plural = _('Light controls')

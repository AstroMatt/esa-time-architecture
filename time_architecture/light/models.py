import datetime

from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import CharField
from django.db.models import PositiveSmallIntegerField
from django.utils.translation import ugettext_lazy as _



class LED(models.Model):
    BOXES = [
        (1, _('Box 1')),
        (2, _('Box 2'))]

    NAMES = [
        ('UVA1', _('UVA1 395nm')),
        ('UVA2', _('UVA2 415nm')),
        ('UVA3', _('UVA3 495nm')),
        ('IR', _('IR 740nm')),
        ('Red', _('Red'))]

    box = PositiveSmallIntegerField(
        verbose_name=_('Box'),
        choices=BOXES,
        db_index=True)

    name = CharField(
        verbose_name=_('Name'),
        max_length=50,
        choices=NAMES,
        db_index=True)

    hour_00 = PositiveSmallIntegerField(
        verbose_name=_('00'),
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text=_('<strong>00:00 - 00:59</strong> - Percent of LED power <strong>[0-100]</strong>%'),
        default=0)

    hour_01 = PositiveSmallIntegerField(
        verbose_name=_('01'),
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text=_('<strong>01:00 - 01:59</strong> - Percent of LED power <strong>[0-100]</strong>%'),
        default=0)
    hour_02 = PositiveSmallIntegerField(
        verbose_name=_('02'),
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text=_('<strong>02:00 - 02:59</strong> - Percent of LED power <strong>[0-100]</strong>%'),
        default=0)
    hour_03 = PositiveSmallIntegerField(
        verbose_name=_('03'),
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text=_('<strong>03:00 - 03:59</strong> - Percent of LED power <strong>[0-100]</strong>%'),
        default=0)
    hour_04 = PositiveSmallIntegerField(
        verbose_name=_('04'),
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text=_('<strong>04:00 - 04:59</strong> - Percent of LED power <strong>[0-100]</strong>%'),
        default=0)
    hour_05 = PositiveSmallIntegerField(
        verbose_name=_('05'),
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text=_('<strong>05:00 - 05:59</strong> - Percent of LED power <strong>[0-100]</strong>%'),
        default=0)
    hour_06 = PositiveSmallIntegerField(
        verbose_name=_('06'),
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text=_('<strong>06:00 - 06:59</strong> - Percent of LED power <strong>[0-100]</strong>%'),
        default=0)
    hour_07 = PositiveSmallIntegerField(
        verbose_name=_('07'),
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text=_('<strong>07:00 - 07:59</strong> - Percent of LED power <strong>[0-100]</strong>%'),
        default=0)
    hour_08 = PositiveSmallIntegerField(
        verbose_name=_('08'),
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text=_('<strong>09:00 - 09:59</strong> - Percent of LED power <strong>[0-100]</strong>%'),
        default=0)
    hour_09 = PositiveSmallIntegerField(
        verbose_name=_('09'),
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text=_('[0-100]% Percent of LED power'),
        default=0)
    hour_10 = PositiveSmallIntegerField(
        verbose_name=_('10'),
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text=_('[0-100]% Percent of LED power'),
        default=0)
    hour_11 = PositiveSmallIntegerField(
        verbose_name=_('11'),
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text=_('[0-100]% Percent of LED power'),
        default=0)
    hour_12 = PositiveSmallIntegerField(
        verbose_name=_('12'),
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text=_('[0-100]% Percent of LED power'),
        default=0)
    hour_13 = PositiveSmallIntegerField(
        verbose_name=_('13'),
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text=_('[0-100]% Percent of LED power'),
        default=0)
    hour_14 = PositiveSmallIntegerField(
        verbose_name=_('14'),
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text=_('[0-100]% Percent of LED power'),
        default=0)
    hour_15 = PositiveSmallIntegerField(
        verbose_name=_('15'),
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text=_('[0-100]% Percent of LED power'),
        default=0)
    hour_16 = PositiveSmallIntegerField(
        verbose_name=_('16'),
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text=_('[0-100]% Percent of LED power'),
        default=0)
    hour_17 = PositiveSmallIntegerField(
        verbose_name=_('17'),
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text=_('[0-100]% Percent of LED power'),
        default=0)
    hour_18 = PositiveSmallIntegerField(
        verbose_name=_('18'),
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text=_('[0-100]% Percent of LED power'),
        default=0)
    hour_19 = PositiveSmallIntegerField(
        verbose_name=_('19'),
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text=_('[0-100]% Percent of LED power'),
        default=0)
    hour_20 = PositiveSmallIntegerField(
        verbose_name=_('20'),
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text=_('[0-100]% Percent of LED power'),
        default=0)
    hour_21 = PositiveSmallIntegerField(
        verbose_name=_('21'),
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text=_('[0-100]% Percent of LED power'),
        default=0)
    hour_22 = PositiveSmallIntegerField(
        verbose_name=_('22'),
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text=_('[0-100]% Percent of LED power'),
        default=0)
    hour_23 = PositiveSmallIntegerField(
        verbose_name=_('23'),
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text=_('[0-100]% Percent of LED power'),
        default=0)

    class Meta:
        ordering = ['box', 'name']
        verbose_name = _('LED')
        verbose_name_plural = _('LEDs')

    def __str__(self):
        return f'Box {self.box} - {self.name}'

    def current_power(self):
        hour = datetime.datetime.now().hour
        power = getattr(self, f'hour_{hour:02d}')
        return {
            'box': self.box,
            'name': self.name,
            'power': power}

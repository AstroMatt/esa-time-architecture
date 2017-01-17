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
        #('White', _('White')),
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
        verbose_name=_('00:00 - 00:59'),
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text=_('[0-100]% Percent of LED power'),
        default=0)

    hour_01 = PositiveSmallIntegerField(
        verbose_name=_('01:00 - 01:59'),
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text=_('[0-100]% Percent of LED power'),
        default=0)
    hour_02 = PositiveSmallIntegerField(
        verbose_name=_('02:00 - 02:59'),
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text=_('[0-100]% Percent of LED power'),
        default=0)
    hour_03 = PositiveSmallIntegerField(
        verbose_name=_('03:00 - 03:59'),
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text=_('[0-100]% Percent of LED power'),
        default=0)
    hour_04 = PositiveSmallIntegerField(
        verbose_name=_('04:00 - 04:59'),
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text=_('[0-100]% Percent of LED power'),
        default=0)
    hour_05 = PositiveSmallIntegerField(
        verbose_name=_('05:00 - 05:59'),
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text=_('[0-100]% Percent of LED power'),
        default=0)
    hour_06 = PositiveSmallIntegerField(
        verbose_name=_('06:00 - 06:59'),
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text=_('[0-100]% Percent of LED power'),
        default=0)
    hour_07 = PositiveSmallIntegerField(
        verbose_name=_('07:00 - 07:59'),
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text=_('[0-100]% Percent of LED power'),
        default=0)
    hour_08 = PositiveSmallIntegerField(
        verbose_name=_('08:00 - 08:59'),
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text=_('[0-100]% Percent of LED power'),
        default=0)
    hour_09 = PositiveSmallIntegerField(
        verbose_name=_('09:00 - 09:59'),
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text=_('[0-100]% Percent of LED power'),
        default=0)
    hour_10 = PositiveSmallIntegerField(
        verbose_name=_('10:00 - 10:59'),
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text=_('[0-100]% Percent of LED power'),
        default=0)
    hour_11 = PositiveSmallIntegerField(
        verbose_name=_('11:00 - 11:59'),
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text=_('[0-100]% Percent of LED power'),
        default=0)
    hour_12 = PositiveSmallIntegerField(
        verbose_name=_('12:00 - 12:59'),
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text=_('[0-100]% Percent of LED power'),
        default=0)
    hour_13 = PositiveSmallIntegerField(
        verbose_name=_('13:00 - 13:59'),
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text=_('[0-100]% Percent of LED power'),
        default=0)
    hour_14 = PositiveSmallIntegerField(
        verbose_name=_('14:00 - 14:59'),
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text=_('[0-100]% Percent of LED power'),
        default=0)
    hour_15 = PositiveSmallIntegerField(
        verbose_name=_('15:00 - 15:59'),
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text=_('[0-100]% Percent of LED power'),
        default=0)
    hour_16 = PositiveSmallIntegerField(
        verbose_name=_('16:00 - 16:59'),
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text=_('[0-100]% Percent of LED power'),
        default=0)
    hour_17 = PositiveSmallIntegerField(
        verbose_name=_('17:00 - 17:59'),
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text=_('[0-100]% Percent of LED power'),
        default=0)
    hour_18 = PositiveSmallIntegerField(
        verbose_name=_('18:00 - 18:59'),
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text=_('[0-100]% Percent of LED power'),
        default=0)
    hour_19 = PositiveSmallIntegerField(
        verbose_name=_('19:00 - 19:59'),
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text=_('[0-100]% Percent of LED power'),
        default=0)
    hour_20 = PositiveSmallIntegerField(
        verbose_name=_('20:00 - 20:59'),
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text=_('[0-100]% Percent of LED power'),
        default=0)
    hour_21 = PositiveSmallIntegerField(
        verbose_name=_('21:00 - 21:59'),
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text=_('[0-100]% Percent of LED power'),
        default=0)
    hour_22 = PositiveSmallIntegerField(
        verbose_name=_('22:00 - 22:59'),
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text=_('[0-100]% Percent of LED power'),
        default=0)
    hour_23 = PositiveSmallIntegerField(
        verbose_name=_('23:00 - 23:59'),
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text=_('[0-100]% Percent of LED power'),
        default=0)

    def __str__(self):
        return f'Box {self.box} - Diode {self.name}'

    class Meta:
        verbose_name = _('LED')
        verbose_name_plural = _('LEDs')

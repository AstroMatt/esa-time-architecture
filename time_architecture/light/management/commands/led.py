import json
from django.core.management.base import BaseCommand, CommandError
from time_architecture.light.models import LED


class Command(BaseCommand):
    help = 'Display LED power status for current hour'

    def handle(self, *args, **options):
        power = [led.current_power() for led in LED.objects.all()]
        output = json.dumps(power)
        self.stdout.write(output)

from django.core.management.base import BaseCommand
from dz_sem2app.models import Client


class Command(BaseCommand):
    help = "Get all clients."

    def handle(self, *args, **kwargs):
        client = Client.objects.all()
        self.stdout.write(f'{client}')
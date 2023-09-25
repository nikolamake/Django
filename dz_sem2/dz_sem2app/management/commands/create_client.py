from django.core.management.base import BaseCommand
from dz_sem2app.models import Client


class Command(BaseCommand):
    help = "Create client."

    def handle(self, *args, **kwargs):
        client = Client(
            name=f'Micha',
            email=f'medved@mail.ru',
            number_phone=f'+(7)33333333',
            address=f'Bryansk'
        )
        client.save()
        self.stdout.write(f'{client}')
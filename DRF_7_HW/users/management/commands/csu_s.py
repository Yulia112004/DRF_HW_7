from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='staff@sky.pro',
            first_name='Staff',
            last_name='Staffov',
            is_staff=True,
            is_superuser=False,
            is_active=True,

        )

        user.set_password('Admin')
        user.save()
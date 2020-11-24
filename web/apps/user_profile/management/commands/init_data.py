from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db import transaction


class Command(BaseCommand):
    help = 'Create initial project data'

    def handle(self, *args, **options):
        with transaction.atomic():
            self._create_initial_user()

    @staticmethod
    def _create_initial_user():
        if not User.objects.exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@utcc.ac.th',
                password='ictutcc'
            )

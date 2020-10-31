from django.contrib.auth.models import User
from django.core.management import BaseCommand
from django.db import transaction

from web.apps.user_profile.models import UserProfile


class Command(BaseCommand):
    help = 'Create initial project data'

    def handle(self, *args, **options):
        with transaction.atomic():
            self._create_initial_user()

    @staticmethod
    def _create_initial_user():
        if not User.objects.exists():
            user = User.objects.create_superuser(
                username='admin',
                email='adnim@utcc.ac.th',
                password='ictutcc',
            )
            UserProfile.objects.create(
                family_name='admin',
                last_name='admin',
                user=user,
                created_user=user,
                updated_user=user
            )

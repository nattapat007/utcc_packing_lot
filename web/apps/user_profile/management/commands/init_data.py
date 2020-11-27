from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db import transaction

from web.apps.user_profile.models import UserProfile


class Command(BaseCommand):
    help = 'Create initial project data'

    def handle(self, *args, **options):
        with transaction.atomic():
            self._create_initial_user()

    @staticmethod
    def _create_initial_user():
        if not User.objects.exists() and not UserProfile.objects.exists():
            user = User.objects.create_superuser(
                username='admin',
                email='admin@utcc.ac.th',
                password='ictutcc'
            )

            UserProfile.objects.create(
                user=user,
                family_name='ICT',
                last_name='ICT',
                phone_number=00000,
                created_user=user,
                updated_user=user
            )

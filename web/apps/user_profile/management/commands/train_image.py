from django.core.management import BaseCommand
from django.db import transaction


class Command(BaseCommand):
    help = 'Create initial project data'

    def handle(self, *args, **options):
        with transaction.atomic():
            self._train_images_user()

    @staticmethod
    def _train_images_user():
        import ipdb
        ipdb.set_trace()
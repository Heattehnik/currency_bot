from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):

        user, created = User.objects.get_or_create(
            email='admin@admin.admin',
            phone='5555555',
            is_staff=True,
            is_superuser=True
        )
        if created:
            user.set_password('admin')
            user.save()

import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User


class Command(BaseCommand):
    help = "Create users!"

    def add_arguments(self, parser):
        parser.add_argument("--numbers", default=1, type=int)

    def handle(self, *args, **options):
        numbers = options.get("numbers")
        seeder = Seed.seeder()
        seeder.add_entity(
            User,
            numbers,
            {
                "avatar": f"user/profile_photos/P{random.randint(1,22)}.jpg",
                "end_of_voucher": lambda x: datetime.today() + timedelta(days=random.randint(-30, 30)),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{numbers} User created!"))

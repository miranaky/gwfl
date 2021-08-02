import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from goodwords.models import GoodWord
from users.models import User
from diaries.models import Diary


class Command(BaseCommand):

    help = "Create sample diaries!"

    def add_arguments(self, parser):
        parser.add_argument("--numbers", default=1, type=int)

    def handle(self, *args, **options):

        numbers = options.get("numbers")
        seeder = Seed.seeder()
        users = User.objects.all()
        goodwords = GoodWord.objects.all()
        seeder.add_entity(
            Diary,
            numbers,
            {
                "author": lambda x: random.choice(users),
                "goodwords": lambda x: random.choice(goodwords),
            },
        )
        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"create {numbers} diaries!"))

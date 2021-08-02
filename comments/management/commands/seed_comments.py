import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User
from diaries.models import Diary
from comments.models import Comment


class Command(BaseCommand):

    help = "Create sample comments!"

    def add_arguments(self, parser):
        parser.add_argument("--numbers", default=1, type=int)

    def handle(self, *args, **options):

        numbers = options.get("numbers")
        seeder = Seed.seeder()
        users = User.objects.all()
        diaries = Diary.objects.all()
        seeder.add_entity(
            Comment,
            numbers,
            {
                "author": lambda x: random.choice(users),
                "diary": lambda x: random.choice(diaries),
            },
        )
        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"create {numbers} comments!"))

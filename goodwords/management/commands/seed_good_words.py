from calendar import monthrange
from django.core.management.base import BaseCommand
from django.utils import timezone
from django_seed import Seed
from goodwords.models import GoodWord, BackgroundPhoto
from calendars.models import Calendar


class Command(BaseCommand):

    help = "Create sample good words for user!"

    def add_arguments(self, parser):
        default_year = timezone.datetime.now().year
        default_month = timezone.datetime.now().month
        parser.add_argument("--year", type=int, default=default_year, help="Set the year to create the good words.")
        parser.add_argument("--month", type=int, default=default_month, help="Set the month to create the good words.")

    def create_calendar(self, year, month):
        """Create monthly calendar"""
        num_days = monthrange(year, month)[1]
        flag = True
        for d in range(1, num_days + 1):
            date = f"{year}-{month}-{d}"
            try:
                Calendar.objects.get(date=date)
                flag = False
            except Calendar.DoesNotExist:
                Calendar.objects.create(date=date)
                flag = True
        if flag:
            self.stdout.write(self.style.SUCCESS(f"Create {year}-{month} calendar."))
        else:
            self.stdout.write(self.style.ERROR(f"{year}-{month} calendar already created!."))

    def create_good_words(self, year, month):
        """Create monthly good words."""
        num_days = monthrange(year, month)[1]
        flag = True
        seeder = Seed.seeder()
        for d in range(1, num_days + 1):
            date = f"{year}-{month}-{d}"
            date_obj = Calendar.objects.get(date=date)
            try:
                GoodWord.objects.get(date=date_obj)
                flag = False
                continue
            except GoodWord.DoesNotExist:
                flag = True
                gw = GoodWord.objects.create(
                    title=seeder.faker.sentence(),
                    goodwords=seeder.faker.sentence(nb_words=10),
                    speaker=seeder.faker.name(),
                    date=date_obj,
                )
                _month = str(month) if month > 10 else f"0{month}"
                BackgroundPhoto.objects.create(
                    caption=seeder.faker.sentence(),
                    goodword=gw,
                    photo=f"goodword/backgrounds/{_month}.jpg",
                )
        if flag:
            self.stdout.write(self.style.SUCCESS(f"Create {year}-{month} good words."))
        else:
            self.stdout.write(self.style.ERROR(f"{year}-{month} good words already created."))

    def handle(self, *args, **options):

        year = int(options.get("year"))
        month = int(options.get("month"))
        self.create_calendar(year, month)
        self.create_good_words(year, month)

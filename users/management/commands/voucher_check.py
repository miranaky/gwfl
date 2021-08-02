from django.core.management.base import BaseCommand
from users.models import User
from django.utils import timezone


class Command(BaseCommand):
    """check end of voucher date and change voucher status."""

    def add_arguments(self, parser):
        parser.add_argument("--check", action="store_true")
        parser.add_argument("--number", action="store_true")

    def handle(self, *args, **options):
        if options["check"]:
            voucher_users = User.objects.filter(voucher=True)
            counter = 0
            for v_user in voucher_users:
                eov = v_user.end_of_voucher
                today = timezone.datetime.today().date()
                if eov < today:
                    v_user.voucher = False
                    v_user.save()
                    counter = +1
            self.stdout.write(self.style.SUCCESS(f"{counter} users finished voucher."))

        if options["number"]:
            voucher_users = User.objects.filter(voucher=True)
            self.stdout.write(self.style.SUCCESS(f"{len(voucher_users)} users have a voucher."))

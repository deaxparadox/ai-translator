from typing import Any
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.core.management.base import BaseCommand, CommandError, CommandParser

from uuid import uuid4

from app.models import LTSAPIToken

class Command(BaseCommand):
    help = "Create the super user programmtically"

    def add_arguments(self, parser: CommandParser) -> None:
        # return super().add_arguments(parser)
        parser.add_argument("USERNAME", type=str)
        parser.add_argument("PASSWORD", type=str)

    def handle(self, *args: Any, **options: Any) -> str | None:
        # for poll_id in options["poll_ids"]:
        USERNAME: str = options['USERNAME']
        PASSWORD: str = options['PASSWORD']
        try:
            user = User.objects.create_user(username=USERNAME, password=PASSWORD)
            LTSAPIToken.objects.create(user=user, token=str(uuid4()))
        except User.MultipleObjectsReturned:
            raise CommandError("User already exists.")
        except IntegrityError as e:
            raise CommandError(e)

        self.stdout.write(
            self.style.SUCCESS("User created successfully.")
        )
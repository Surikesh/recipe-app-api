"""
Django command for waiting for database to be available before continuing
"""
import time
from psycopg2 import OperationalError as Psycopg2Error
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Django command to pause execution until database is available"""

    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')
        db_up = False
        self.stdout.write('Database available!')
        while not db_up:
            try:
                self.check(databases=['default'])
                db_up = True
                self.stdout.write(self.style.SUCCESS('Database available!'))
            except (Psycopg2Error, OperationalError):
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)

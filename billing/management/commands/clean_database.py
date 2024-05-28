from typing import Any
from django.core.management.base import BaseCommand
from django.db import connection
from django.conf import settings

class Command(BaseCommand):
    help = 'Cleans the database by truncating all tables'

    def handle(self, *args, **kwargs):
        if not settings.DEBUG:
            self.stdout.write(self.style.ERROR('This command can only be run in DEBUG mode'))
            return

        confirmation = input("Are you sure you want to delete all data in the database? This action cannot be undone. Type 'yes' to continue: ")
        if confirmation != 'yes':
            self.stdout.write(self.style.WARNING('Database cleaning aborted'))
            return

        with connection.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
            tables = connection.introspection.table_names()
            for table in tables:
                cursor.execute(f'TRUNCATE TABLE `{table}`;')
            cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")

        self.stdout.write(self.style.SUCCESS('Successfully cleaned the database'))

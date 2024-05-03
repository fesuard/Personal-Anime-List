from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):
    help = "Delete database table associated with a deleted model"

    def handle(self, *args, **options):
        table_name = "animeList_anime"  # Replace with your actual model table name
        with connection.cursor() as cursor:
            cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
            self.stdout.write(self.style.SUCCESS(f"Deleted table: {table_name}"))

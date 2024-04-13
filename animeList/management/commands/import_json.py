import json
from django.core.management.base import BaseCommand
from animeList.models import Anime


class Command(BaseCommand):
    help = 'Import external JSON file data into Django database'

    def handle(self, *args, **kwargs):
        with open(r'C:\Users\fesua\PycharmProjects\final_project\pal\animeList\animesJson.json', 'r',
                  encoding='utf8') as jfile:
            data = json.load(jfile)

            for item in data:
                Anime.objects.create(
                    title=item['title'],
                    type=item['type'],
                    episodes=item['episodes'],
                    status=item['status'],
                    year=item['year'],
                    season=item['season'],
                    picture=item['picture'],
                    thumbnail=item['thumbnail'],
                    relatedAnime=item['relatedAnime'],
                    tags=item['tags']
                )
        self.stdout.write(self.style.SUCCESS("Done"))

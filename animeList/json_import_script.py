
import json
from animeList.models import Anime


def import_json(path):
    with open(path, encoding='utf8') as jfile:
        data = json.load(jfile)

        for anime in data:
            Anime.objects.create(
                title=anime['title'],
                type=anime['type'],
                episodes=anime['episodes'],
                status=anime['status'],
                year=anime['year'],
                season=anime['season'],
                picture=anime['picture'],
                thumbnail=anime['thumbnail'],
                relatedAnime=anime['relatedAnime'],
                tags=anime['tags']
            )


if __name__ == '__main__':
    import_json('animesJson.json')

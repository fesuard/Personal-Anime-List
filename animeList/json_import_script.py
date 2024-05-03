import json
import os

import django

# urmatoarele 2 linii sunt pentru a ne permite importul extern cu scriptul de mai jos, trebuie sa fie adaugate inainte
# sa importam modelul
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pal.settings")
django.setup()


def import_json(path):
    from animeList.models import Anime, Tag

    with open(path, encoding="utf8") as jfile:
        data = json.load(jfile)

        for anime in data:

            db_anime = Anime(
                title=anime["title"],
                type=anime["type"],
                episodes=anime["episodes"],
                status=anime["status"],
                year=(
                    int(anime["year"])
                    if anime["year"]
                    not in [
                        "",
                        None,
                    ]
                    else 0
                ),
                season=anime["season"],
                picture=anime["picture"],
                thumbnail=anime["thumbnail"],
                relatedAnime=anime["relatedAnime"],
            )
            db_anime.save()  # save se face si aici ca sa poata sa gaseasca mai jos db_anime.tags, altfel nu ar exista
            for t in anime["tags"]:
                db_tag, created = Tag.objects.get_or_create(name=t)
                db_anime.tags.add(db_tag)
            db_anime.save()


if __name__ == "__main__":
    import_json("animesJson.json")

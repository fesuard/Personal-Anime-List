import json


def parse_json(path, newFilePath):
    final_list = []
    with open(path, encoding='utf8') as jfile:
        data = json.load(jfile)
        for elem in data:
            if elem == 'data':
                for field in data[elem]:
                    season = field['animeSeason']
                    new_dict = {
                        'title': field['title'],
                        'type': field['type'],
                        'episodes': field['episodes'],
                        'status': field['status'],
                        'year': season['year'],
                        'season': season['season'],
                        'picture': field['picture'],
                        'thumbnail': field['thumbnail'],
                        'relatedAnime': field['relatedAnime'],
                        'tags': field['tags']
                    }
                    final_list.append(new_dict)

    with open(newFilePath, 'w') as newJsonFile:
        json.dump(final_list, newJsonFile, indent=4)

    jfile.close()
    newJsonFile.close()


if __name__ == '__main__':
    parse_json('../anime-offline-database.json', 'animesJson.json')

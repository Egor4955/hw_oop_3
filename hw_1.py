import requests
import json

heroes_list = ['Hulk', 'Captain America', 'Thanos']
id_ = []

url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'

hero_dict = json.loads(requests.get(url).content)
id_list = []
hero_list = []

for id_hero in hero_dict:
    id_list.append(','.join([str(id_hero['id'])])) 

for hero_name in hero_dict:
    hero_list.append(','.join([str(hero_name['name'])])) 

name_id_hero = dict(zip(hero_list, id_list))

for hero in heroes_list:
    id_.append(name_id_hero.get(hero))

my_hero_id_dict = dict(zip(heroes_list, id_))
int_list = []
for id_num in id_:
    req = requests.get(f'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/powerstats/{id_num}.json')
    req1 = json.loads(req.content)
    int_list.append(req1["intelligence"])

hero_intelligence_dict = dict(sorted(zip(heroes_list, int_list)))
x = list(hero_intelligence_dict.items())
print(f'Самым умным супергероем является {x[-1]}')


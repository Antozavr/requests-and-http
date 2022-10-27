import requests
from pprint import pprint


def smartest():
    heroes_list = []
    res = requests.get('https://akabab.github.io/superhero-api/api/all.json')
    for i in res.json():
        if i['name'] == 'Hulk':
            heroes_list.append(i)
        elif i['name'] == 'Captain America':
            heroes_list.append(i)
        elif i['name'] == 'Thanos':
            heroes_list.append(i)
        else:
            continue
    cap = heroes_list[0]
    a = cap['powerstats']
    hulk = heroes_list[1]
    b = hulk['powerstats']
    thanos = heroes_list[2]
    c = thanos['powerstats']
    top_stat = max(a["intelligence"], b["intelligence"], c["intelligence"])
    for name in heroes_list:
        if name['powerstats']['intelligence'] == top_stat:
            print(name['name'])


if __name__ == '__main__':
    smartest()

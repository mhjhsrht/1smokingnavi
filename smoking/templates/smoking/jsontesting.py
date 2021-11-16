import json
from django.shortcuts import render, HttpResponse
import requests, urlopen

def showattractions(request):
    with urlopen(
            'https://raw.githubusercontent.com/mhjhsrht/1smokingnavi/main/smoking/static/charts/smokingarea.json') as response:
        attractions = json.load(response)

    attractiondict = []
    for attraction in attractions:
        if attraction.get('mapx'):
            content = {
                "title": attraction['title'],
                "mapx": str(attraction['mapx']),
                "mapy": str(attraction['mapy']),
                "addr1": str(attraction['addr1']),
            }

            attractiondict.append(content)
    attractionJson = json.dumps(attractiondict, ensure_ascii=False)

    return render(request, 'smoking/area.html', {'attractionJson': attractionJson})


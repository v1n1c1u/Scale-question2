"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.http import JsonResponse
import json


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html'   
    )

#api de'https://www.amock.io/api/fcmaia/countries' mas com a chave 'name' entre aspas
def api(request):
    api = [
	{"code": "COL", "name": "COLOMBIA", "fronteiras": ["BRA", "ECU", "PAN", "PER", "VEN" ] },
    {"code": "BRA", "name": "BRASIL", "fronteiras": [ "ARG", "BOL", "COL", "GUF", "GUY", "PRY", "PER", "SUR", "URY", "VEN" ] },
	{"code": "ECU", "name": "EQUADOR", "fronteiras": [ "COL", "PER" ] },
    {"code": "PAN", "name": "PANAMA", "fronteiras": [ "COL" ] },
	{"code": "PER", "name": "PERU", "fronteiras": [ "BOL", "BRA", "CHL", "COL", "ECU" ] },
    {"code": "VEN", "name": "VENEZUELA", "fronteiras": [ "BRA", "COL", "GUY" ] },
	{"code": "ARG", "name": "ARGENTINA", "fronteiras": [ "BOL", "BRA", "CHL", "PRY", "URY" ] },
    {"code": "BOL", "name": "BOLIVIA", "fronteiras": [ "ARG", "BRA", "CHL", "PRY", "PER" ] },
	{"code": "GUF", "name": "GUIANA FRANCESA", "fronteiras": [ "BRA", "SUR", "VEN" ] },
    {"code": "PRY", "name": "PARAGUAI", "fronteiras": [ "BRA", "GUF", "GUY" ] },
	{"code": "SUR", "name": "SURINAME", "fronteiras": [ "BRA", "GUF", "GUY" ] },
    {"code": "URY", "name": "URUGUAI", "fronteiras": [ "ARG", "BRA" ] },
    {"code": "CHL", "name": "CHILE", "fronteiras": [ "ARG", "BOL", "PER" ] }
	]

    return JsonResponse(api, safe=False)
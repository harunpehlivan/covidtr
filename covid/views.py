from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
# Create your views here.

def index(request):
  data = json.loads(requests.get("https://covid19.mathdro.id/api").text)
  countries = json.loads(requests.get("https://covid19.mathdro.id/api/countries").text)
  return render(request, "index.html", {
    "data": data,
    "countries": countries
  })
def country(request, country):
  data = json.loads(requests.get("https://covid19.mathdro.id/api/countries/" + country).text)
  countries = json.loads(requests.get("https://covid19.mathdro.id/api/countries").text)
  return render(request, "country.html", {
    "data": data,
    "country": country,
    "countries": countries
  })
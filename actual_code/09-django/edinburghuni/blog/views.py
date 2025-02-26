from django.http import JsonResponse
from .models import Post
from django.core.serializers import serialize
import json
import requests
from django.views.decorators.cache import cache_page
# Create your views here.

def hello_world(request):
    print(request)
    return JsonResponse({"message": "hello world"})

def show_all_posts(request):
    posts = serialize("json", Post.objects.all())
    print(posts)
    return JsonResponse({"posts": json.loads(posts)})

@cache_page(10)
def get_country_details(request, country):
    print("Queried API")
    response = requests.get(f"https://restcountries.com/v3.1/name/{country}")
    if response.status_code == 200:
        country_data = response.json()
        if country_data:
            details = {
                "name": country,
                "tld": country_data[0]["tld"][0],
                "flag": country_data[0]["flag"],
                "api_version": 1
            }
            return JsonResponse(details)
    else:
        return JsonResponse({"message": "Can't find country details"})
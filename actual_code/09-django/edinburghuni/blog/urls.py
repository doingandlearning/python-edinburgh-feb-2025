from django.urls import path
from .views import hello_world, show_all_posts, get_country_details

urlpatterns =  [
    path('api/hello', hello_world, name="hello_world"),
    path('api/posts', show_all_posts, name="show_all_posts"),
    path('api/country/<str:country>', get_country_details, name="get_country_details")
]
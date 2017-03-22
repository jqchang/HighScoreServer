from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^submit$',views.submit),
    url(r'^api/scores$',views.scoresJson),
    url(r'^api/scores/(?P<rank>\d+)$', views.byRank)
]

from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    url(r'^miners$', views.MinersList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
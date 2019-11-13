from django.urls import path, include
from wiki.views import PageListView, PageDetailView
from django.conf.urls import url
from .views import SignUpView

urlpatterns = [
    url(r'signup$', SignUpView.as_view(), name='signup'),
]

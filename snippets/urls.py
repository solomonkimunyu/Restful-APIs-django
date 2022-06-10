from django.urls import path
from .views import SnippetList, SnippetDetail
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('snippets/', SnippetList.as_view(), name='listview'), 
    path('snippets/<int:pk>/', SnippetDetail.as_view()),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)
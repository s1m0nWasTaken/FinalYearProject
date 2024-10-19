from django.urls import path
from .views import register, login, cast_vote, results

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('cast_vote/', cast_vote, name='cast_vote'),
    path('results/', results, name='results'),
]
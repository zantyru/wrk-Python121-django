from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='application-index'),
    path('<int:question_id>/', views.detail, name='application-detail'),
    path('<int:question_id>/results/', views.results, name='application-results'),
    path('<int:question_id>/vote/', views.vote, name='application-vote'),
]

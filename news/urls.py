from django.urls import path, include
from news import views
from google_trends.views import TrendsView

urlpatterns = [
    path('', TrendsView.as_view()),
    path('generate-news/', views.generate_news),
]

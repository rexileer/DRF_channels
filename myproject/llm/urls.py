from django.urls import path

from . import views


urlpatterns = [
    path('response/', views.llm_response, name='llm_response'),
]

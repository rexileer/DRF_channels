from django.contrib import admin
from django.urls import path

import views


urlpatterns = [
    path('response/', views.llm_response, name='llm_response'),
]

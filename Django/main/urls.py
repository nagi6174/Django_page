from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),  # name = "index" を追加
    path("<int:question_id>/", views.detail, name="detail"),
]
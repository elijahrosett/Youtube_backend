from django.urls import path
from. import views

urlpatterns = [
    path('replies/all', views.get_all),
    path('replies/<pk>', views.replys_by_comment),
]
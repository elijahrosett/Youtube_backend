from django.urls import path
from. import views

urlpatterns = [
    path('', views.comment_replys),
    path('all/', views.get_all),
    path('<pk>/', views.replys_by_comment),
]
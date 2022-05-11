from django.urls import path, include
from . import views

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<

urlpatterns = [
    path('', views.user_comments),
    path('all/', views.get_all),
    path('<pk>/', views.comments_by_detail),
    path('<pk>/update/', views.comments_by_detail),

]

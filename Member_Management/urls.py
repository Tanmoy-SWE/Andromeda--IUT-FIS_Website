from django.urls import path
from . import views

urlpatterns = [
    path('', views.memberHome, name='memberHome'),
    path('member/view_all_member/', views.view_all_member, name='view_all_member'),
    path('member/add_member/', views.add_member, name='add_member'),
    path('remove_member/', views.remove_member, name='remove_member'),
    path('filter_member/', views.filter_member, name='filter_member'),
]
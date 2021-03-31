from django.urls import path
from . import views


urlpatterns =[
    path('', views.index),
    path('create_user', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('success', views.success),
    path('user/<int:id>', views.profile),
    path('create_message', views.create_message),
    path('create_comment', views.create_comment),
    path('comment_delete/<int:id>', views.delete_comment),
    path('delete/<int:id>', views.delete_message)
]
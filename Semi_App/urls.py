from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.listShows),
    path('new', views.addshow),
    path('edit/<int:show_id>', views.edit),
    path('view/<int:show_id>', views.viewShow),
    path('update/<int:show_id>', views.updateCreateShow),
    path('createShow', views.createShow),
    path('delete/<int:show_id>', views.deleteShow)
]
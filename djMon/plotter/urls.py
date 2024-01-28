from django.urls import path
from .import views

app_name = 'plotter'
urlpatterns = [
    path('', views.index, name='plotter'),
    path('add/', views.add_point, name ='point_add'),
    path('show/', views.get_all_points, name = 'point_show'),
]
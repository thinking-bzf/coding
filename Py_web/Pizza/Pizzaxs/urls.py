from . import views
from django.urls import path,re_path

app_name = 'Pizzaxs'
urlpatterns = [
    path('', views.index, name='index'),
    path('Pizzas/', views.Pizzas, name='Pizzas'),
    # path('Pizzas/<str:pizza_name>/', views.Seasoning, name='Seasoning')
    re_path(r'^Pizzas/(?P<pizza_id>\d+)/$',views.Seasoning, name='Seasoning'),
]

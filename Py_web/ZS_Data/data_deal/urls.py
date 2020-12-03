from django.urls import path, re_path
from . import views

app_name = 'data_deal'

urlpatterns = [
    path('', views.index, name='index'),
    path('FirstZY/', views.FirstZY_deal, name='FirstZY'),
    path('FirstZY/<str:file_name>/', views.FirstZY_dl, name='FirstZY_dl'),
    path('Original/', views.original, name='original'),
    path('Original_index/', views.original_index, name='original_index'),
    path('OriginalMerge_index/', views.OriginalMerge_index,
         name='OriginalMerge_index'),
#     path('Original_merge/', views.original_merge, name='original_merge'),
    path('Original/<str:year>/<str:date_time>/<str:file_name>/',
         views.original_dl, name='original_dl'),
    path('Data_CleanDL/<str:year>/<str:date_time>/<str:file_name><str:s>/',
         views.Data_CleanDL, name='Data_CleanDL'),
    path('Data_clean/<str:year>/<str:date_time>/<str:file_name>/<int:file_id>/',
         views.data_clean, name='DataClean'),
    path('Today_clean/<str:date>/',
         views.Today_clean, name='TodayClean'),
    path('Today_Merge/<str:date>/',
         views.Today_Merge, name='TodayMerge'),
    path('Today_cleanDL/<str:date>/',
         views.Today_cleanDL, name='TodayClean_DL')

]

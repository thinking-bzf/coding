from django.urls import path, re_path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.index, name='index'),
    path('new_blog/', views.new_blog, name='new_blog'),
    path('<int:user_id>/new_blog/',
         views.personal_new_blog, name='personal_new_blog'),
    # path('<int:blog_id>/', views.edit_blog, name='edit_blog'),
    path('<int:user_id>/', views.personal_index, name='personal'),
    path('<int:user_id>/<int:blog_id>_edit/',
         views.personal_edit_blog, name='personal_edit_blog'),
    path('<int:ownerid>/<str:ownername>_view/',
         views.user_page, name='userpage'),
]

from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static

app_name='WebApplication'
urlpatterns = [
    path('', login_required(views.home), name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('edit/<str:tag_id>', login_required(views.edit), name='edit'),
    path('logout/', login_required(views.logout), name='logout'),
    path('delete/<str:tag_id>', login_required(views.delete), name='delete'),
    path('add/', login_required(views.add), name='add'),
    path('/<str:tag_id>', login_required(views.item), name='item'),
    path('not_allow/', login_required(views.not_allow), name='not_allow'),
    path('edit_notallow/<str:date_time>',login_required(views.editNotAllow), name='editNotAllow'),


]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
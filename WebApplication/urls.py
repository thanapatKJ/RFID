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
    path('item/<str:tag_id>/', login_required(views.item), name='item'),
    path('not_allow/', login_required(views.not_allow), name='not_allow'),
    path('not_allow/<str:id>', login_required(views.delete_nl), name='delete_nl'),
    path('item_notallow/<str:id>',login_required(views.editNotAllow), name='editNotAllow'),
    path('delete_history/<str:id>', login_required(views.delete_history), name='deleteHistory'),
    path('notfound/',login_required(views.notFound), name='notFound'),
    path('notfound/deleteNF/<str:id>',login_required(views.deleteNF), name='deleteNF'),
    path('notfound/itemNF/<str:id>',login_required(views.itemNF), name='itemNF'),
    path('report/',login_required(views.report), name='report'),
    path('reportF/<str:date>',login_required(views.reportF), name='reportF'),



]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
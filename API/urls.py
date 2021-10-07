from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name='API'
urlpatterns = [
    path('getAllItem/',views.getAllItem, name='getAllItem'),
    path('getAllNotAllowed',views.getAllNotAllowed, name='getAllNotAllowed'),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
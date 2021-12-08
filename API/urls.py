from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name='API'
urlpatterns = [
    path('getAllItem/',views.getAllItem, name='getAllItem'),
    path('getAllNotAllowed/',views.getAllNotAllowed, name='getAllNotAllowed'),
    path('tagData/',views.tagData.as_view(), name='tagData'),
    path('notAllowed/',views.notAllowed.as_view(), name='notAllowed'),
    path('notFound/',views.notFound.as_view(), name='notFound'),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
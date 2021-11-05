from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views as invitation_views

urlpatterns = [
    path('', invitation_views.invitation, name='invitation'),
    path('check/', invitation_views.check, name='check'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
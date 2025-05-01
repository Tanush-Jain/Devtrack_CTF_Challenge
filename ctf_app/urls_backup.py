from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect
from ctf import views

def redirect_to_participant_login(request):
    return redirect('participant_login')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),
    path('admin_portal/', views.admin_portal, name='admin_portal'),
    path('participant_login/', views.participant_login, name='participant_login'),
    path('participant_page/', views.participant_page, name='participant_page'),
    path('participant_scores/', views.participant_scores, name='participant_scores'),
    path('participant/', redirect_to_participant_login),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])


from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from taken_by import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    
    path('teacher/', include('teacher.urls'),name='teacher'),
    path('course/', include('course.urls'),name='course'),
    path('sem/', include('semester.urls'),name='sem'),
    path('batch/', include('batch.urls'),name='batch'),
    path('cr/', include('CR.urls'),name='cr'),
    path('taken/', include('taken_by.urls'),name='taken'),
    path('final/', include('final.urls'),name='final'),
    
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
  
    
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


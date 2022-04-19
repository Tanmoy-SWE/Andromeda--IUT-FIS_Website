from django.urls import path
from . import views
from .AstroInfo import issLocation, astroPhotoDay, marsPhotos
from django.conf.urls.static import static
from django.conf import settings 



urlpatterns = [
    path('', views.home, name='home'),
    path('homeAdmin/', views.homeAdmin, name='homeAdmin'),
    path('register/', views.registerPage, name= 'register'),
    path('login/', views.loginPage, name= 'login'),
    path('logout/', views.logoutUser, name= 'logout'),
    path('ISSLocation/', issLocation.isslocation, name='ISSLocation'),
    path('astroPhotoDay/', astroPhotoDay.astroPhotoOftheDay, name='astroPhotoDay'),
    path('astroPhotoYesterday/', astroPhotoDay.astroPhotoOfYesterday, name='astroPhotoOfYesterday'),
    path('marsPhotos/', marsPhotos.marsPhotos, name='marsPhotos'),
    path('index/', views.solarsystem, name='index'),
    path('news/', views.news, name='news')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
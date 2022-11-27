from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.home, name = 'home'),
    path('club', views.clubView, name = 'club'),
    path('club/<int:id>', views.clubDetailView, name = 'club_detail'),
    path('facility', views.facilityView, name = 'facility'),
    path('facility/<int:id>', views.facilityDetailView, name = 'facility_detail'),
    path('postcreate/', views.postCreate, name = "post_create"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


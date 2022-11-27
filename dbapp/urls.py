from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.home, name = 'home'),
    path('club', views.clubView, name = 'club'),
    path('clubcreate', views.clubCreate, name = "club_create"),
    path('club/<int:id>', views.clubDetailView, name = 'club_detail'),
    path('club/<int:id>/delete', views.clubDelete, name = 'club_delete'),
    path('club/<int:id>/update', views.clubUpdate, name = 'club_update'),
    path('facility', views.facilityView, name = 'facility'),
    path('facilitycreate', views.facilityCreate, name = "facility_create"),
    path('facility/<int:id>', views.facilityDetailView, name = 'facility_detail'),
    path('facility/<int:id>/delete', views.facilityDelete, name = 'facility_delete'),
    path('facility/<int:id>/update', views.facilityUpdate, name = 'facility_update'),
    path('postcreate/', views.postCreate, name = "post_create"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


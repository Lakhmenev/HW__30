from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from ads import views
from locations.views import LocationViewSet


router = routers.SimpleRouter()
router.register(r'location', LocationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ads),
    path('ad/', views.AdListView.as_view()),
    path('ad/<int:pk>/', views.AdDetailView.as_view()),
    path('ad/create/', views.AdCreateView.as_view()),
    path('ad/<int:pk>/update/', views.AdUpdateView.as_view()),
    path('ad/<int:pk>/delete/', views.AdDeleteView.as_view()),
    path('ad/<int:pk>/upload_image/', views.AdUploadImageView.as_view()),
    path('user/', include("authentication.urls")),
    path('cat/', include('categories.urls')),
    path('location/', include('locations.urls')),
    path('selection/', include('selections.urls')),
]

urlpatterns += router.urls


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

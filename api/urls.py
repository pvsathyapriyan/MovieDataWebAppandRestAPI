from django.urls import include, path
from rest_framework import routers
from . import views

#api URLs for two models 
router = routers.DefaultRouter()
router.register(r'movies', views.MoviesViewSet)
router.register(r'category', views.CategoryViewSet)


urlpatterns = [
    path('', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
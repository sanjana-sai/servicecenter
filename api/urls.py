from django.urls import path

from api import views

from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register("customers",views.CustomerViewsetView,basename="customers")


urlpatterns=[

    path("token/",ObtainAuthToken.as_view()),

    path("customers/<int:pk>/work/",views.WorkCreativeView.as_view()),
    
    path("work/<int:pk>/",views.WorkDetailView.as_view()),

]+router.urls
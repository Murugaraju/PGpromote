from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CustomerModelViewSet,PackagePaymentModelViewSet,PGModelViewSet,PGDetailsModelViewSet

router=DefaultRouter()
router.register(r'customer',CustomerModelViewSet)
router.register(r'packagepayment',PackagePaymentModelViewSet)
router.register(r'pg',PGModelViewSet)
router.register(r'pgdetails',PGDetailsModelViewSet)


urlpatterns = [

   path('',include(router.urls))
]
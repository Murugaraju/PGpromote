from django.shortcuts import render
from .serializers import PGDetailsModelSerializer,CustomerModelSerializer,PackagePaymentModelSerializer,PGModelSerializer
from .models import PG,Customer,PGDetails,PackagePayment
from rest_framework.viewsets import ModelViewSet
# Create your views here.


class CustomerModelViewSet(ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class=CustomerModelSerializer


class PackagePaymentModelViewSet(ModelViewSet):
    queryset=PackagePayment.objects.all()
    serializer_class=PackagePaymentModelSerializer



class PGModelViewSet(ModelViewSet):
    queryset=PG.objects.all()
    serializer_class=PGModelSerializer

    

class PGDetailsModelViewSet(ModelViewSet):
    queryset=PGDetails.objects.all()
    serializer_class=PGDetailsModelSerializer

    
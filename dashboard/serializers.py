from rest_framework.serializers import ModelSerializer
from .models import PG,Customer,PGDetails,PackagePayment



class CustomerModelSerializer(ModelSerializer):
    class Meta:
        model=Customer
        fields='__all__'


class PackagePaymentModelSerializer(ModelSerializer):
    class Meta:
        model=PackagePayment
        fields='__all__'



class PGModelSerializer(ModelSerializer):
    class Meta:
        model=PG
        fields='__all__'



class PGDetailsModelSerializer(ModelSerializer):
    class Meta:
        model=PGDetails
        fields='__all__'
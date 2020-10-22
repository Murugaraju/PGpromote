from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name=models.CharField(max_length=150)
    last_name=models.CharField(max_length=150)
    created_at=models.DateTimeField(auto_now=True)
    mobile_no=models.CharField(max_length=10,unique=True)


class PackagePayment(models.Model):
    package_choices=[
        ('Q','Quarter'),
        ('H','Half'),
        ('Y','Year'),



    ]

    customerob=models.OneToOneField('Customer',on_delete=models.CASCADE)
    service_package_name=models.CharField(max_length=100,choices=package_choices,default='Q')
    start_date=models.DateTimeField()
    end_date=models.DateTimeField()

class PG(models.Model):
    pg_name=models.CharField(max_length=120)
    owner=models.ForeignKey('Customer',on_delete=models.CASCADE)
    arealocated=models.CharField(max_length=120)
    famous_landmark=models.CharField(max_length=120)
    pg_type=models.CharField(max_length=50,choices=[('Men','Men'),('Women','Women')])

#below funtion for upload_to attribute of FileField for PGDetails Model
def pg_name_get(instance,filename):
    return 'images/'+str(instance.pg_ob.pg_name)+'/'+filename
class PGDetails(models.Model):

    pg_ob=models.OneToOneField('PG',on_delete=models.CASCADE)
    main1=models.FileField(upload_to=pg_name_get)
    main2=models.FileField(upload_to=pg_name_get)
    single_sharing=models.FileField(upload_to=pg_name_get)
    double_sharing=models.FileField(upload_to=pg_name_get)
    three_sharing=models.FileField(upload_to=pg_name_get)
    four_sharing=models.FileField(upload_to=pg_name_get)
    kitchen=models.FileField(upload_to=pg_name_get)
    bathroom=models.FileField(upload_to=pg_name_get)
    location=models.FileField(upload_to=pg_name_get)

    # facilities yet to think
    








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


class PGDetails(models.Model):
    pg_ob=models.OneToOneField('PG',on_delete=models.CASCADE)
    main1=models.CharField(max_length=600)
    main2=models.CharField(max_length=600)
    single_sharing=models.CharField(max_length=600)
    double_sharing=models.CharField(max_length=600)
    three_sharing=models.CharField(max_length=600)
    four_sharing=models.CharField(max_length=600)
    kitchen=models.CharField(max_length=600)
    bathroom=models.CharField(max_length=600)
    location=models.CharField(max_length=600)

    # facilities yet to think
    
    







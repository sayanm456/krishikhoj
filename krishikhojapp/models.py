from django.db import models

# Create your models here.
class Tractor(models.Model):
    tractor_id = models.AutoField(primary_key=True)
    tractor_name = models.CharField(max_length=50,default="")

    def __str__(self):
        return self.tractor_name


class Farmer(models.Model):
    farmer_id = models.AutoField
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=15,default=0)
    tractor_name = models.ForeignKey(Tractor, on_delete=models.CASCADE)
    registration_no = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.farmer_id, self.name, self.address, self.contact_no, self.tractor_name, self.registration_no, self.price, self.date





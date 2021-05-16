from django.db import models
from django.utils.timezone import timezone

class Pharmacy(models.Model):
    YES = "yes"
    NO = "no"
    IS_WORKING = (
        (YES, "yes"),
        (NO, "no")
    )
    name = models.CharField(max_length=1024)
    phone_number = models.IntegerField()
    location = models.CharField(max_length=1024)
    is_working = models.CharField(max_length=10, choices=IS_WORKING)

    class Meta:
        db_table = "pharmacy"

    def __str__(self):
        return self.name




class Medicine(models.Model):
    PILL = "pill"
    KAPSULA = "kapsula"
    AMPULA = "ampula"
    GEL = "gel"
    SHAPE = (
        (PILL, "pill"),
        (KAPSULA, "kapsula"),
        (GEL, "gel"),
        (AMPULA, "ampula"),
    )
    name = models.CharField(max_length=1024)
    shape = models.CharField(max_length=256, choices=SHAPE)
    text = models.CharField(max_length=1024)
    made_on = models.DateField()
    yaroqlilik_muddati = models.CharField(max_length=512)

    class Meta:
        db_table = "medicine"

    def __str__(self):
        return self.name




class Distribution(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=512)
    price = models.CharField(max_length=256)

    class Meta:
        db_table = "distribution"

    def __str__(self):
        return f"{self.medicine}  {self.pharmacy}"


from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)
    roll_no    = models.IntegerField(unique="True")
    email      = models.EmailField(max_length=15)
    admission_date = models.DateField()
    fees_paid  = models.DecimalField(max_digits=6, decimal_places=2)

    def __unicode__(self):
        return self.first_name + " " + self.last_name

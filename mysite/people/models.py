from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    emp_id = models.IntegerField()
    email_id = models.EmailField()
    emp_deg = models.CharField(max_length=50)
    department_name = models.CharField(max_length=50)
    reporting_name = models.CharField(max_length=50)
    seating_location = models.CharField(max_length=50)
    mobile_no = models.CharField(max_length=12)
    extn_no = models.CharField(max_length=12,default = '')
    image = models.FileField(upload_to='documents/%Y/%m/%d', default=None, null=True)

    def __str__(self):
        return "{0}, {1}".format(self.last_name, self.first_name)


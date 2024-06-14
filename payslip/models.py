from django.db import models


class Payslip(models.Model):
    job_title = models.CharField(max_length=100)
    net_salary = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10, default='ZMW')
    other_info = models.TextField(blank=True, null=True)
    employment_type = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    file = models.FileField(upload_to='payslips/', blank=True, null=True)
    upload_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.job_title} - {self.net_salary}"

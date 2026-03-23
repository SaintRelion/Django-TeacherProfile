from django.db import models
from sr_libs.dal.mixins import ArchiveMixin


class PersonalInformation(ArchiveMixin):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=50)
    photo_base64 = models.TextField(blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=20)
    civil_status = models.CharField(max_length=20)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=20)
    home_address = models.TextField()
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    employment_status = models.CharField(max_length=50)
    date_hired = models.DateField()
    salary_grade = models.CharField(max_length=20)
    tin = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.employee_id})"

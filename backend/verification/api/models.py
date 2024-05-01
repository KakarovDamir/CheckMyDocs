from django.db import models

class FileData(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file_type = models.CharField(max_length=255)
    doc_type = models.CharField(max_length=255)


class FakeIDCardDB(models.Model):
    issue_date = models.CharField(max_length=20)
    doc_number = models.CharField(max_length=20)
    ssn = models.CharField(max_length=20)


class FakeDriverLicenseDB(models.Model):
    license_number = models.CharField(max_length=20)
    valid_date = models.CharField(max_length=20)


class FakeSATDB(models.Model):
    unique_number = models.CharField(max_length=20)
    sat_ssn = models.CharField(max_length=20)
    sat_ict = models.CharField(max_length=20)
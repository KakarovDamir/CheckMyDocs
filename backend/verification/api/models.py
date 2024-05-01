from django.db import models

class FileData(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file_type = models.CharField(max_length=255)
    doc_type = models.CharField(max_length=255)

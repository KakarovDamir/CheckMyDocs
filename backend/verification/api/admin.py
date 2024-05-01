from django.contrib import admin
from .models import UploadedFile

@admin.register(UploadedFile)
class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ['id', 'file', 'uploaded_at','file_type', 'doc_type']
    list_filter = ['file_type','doc_type',]
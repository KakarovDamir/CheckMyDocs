from django.contrib import admin
from api.models import FileData

@admin.register(FileData)
class FileDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'file', 'uploaded_at','file_type', 'doc_type']
    list_filter = ['file_type','doc_type',]
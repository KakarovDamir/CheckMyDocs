from django.contrib import admin
from api.models import FileData, FakeIDCardDB, FakeDriverLicenseDB

@admin.register(FileData)
class FileDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'file', 'uploaded_at','file_type', 'doc_type']
    list_filter = ['file_type','doc_type',]



@admin.register(FakeDriverLicenseDB)
class FakeDriverLicenseDBAdmin(admin.ModelAdmin):
    list_display = ['id', 'license_number', 'valid_date']
    list_filter = ['valid_date',]


@admin.register(FakeIDCardDB)
class FakeIDCardDBAdmin(admin.ModelAdmin):
    list_display = ['id', 'issue_date', 'doc_number','ssn']
    list_filter = ['issue_date',]
from django.contrib import admin
from api.models import FileData, FakeIDCardDB, FakeDriverLicenseDB, FakeSATDB

@admin.register(FileData)
class FileDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'file', 'uploaded_at','file_type', 'doc_type']
    list_filter = ['file_type','doc_type',]



@admin.register(FakeDriverLicenseDB)
class FakeDriverLicenseDBAdmin(admin.ModelAdmin):
    list_display = ['id', 'license_number', 'valid_date', 'verdict']
    list_filter = ['valid_date',]


@admin.register(FakeIDCardDB)
class FakeIDCardDBAdmin(admin.ModelAdmin):
    list_display = ['id', 'issue_date', 'doc_number','ssn', 'verdict']
    list_filter = ['issue_date',]


@admin.register(FakeSATDB)
class FakeSATDBAdmin(admin.ModelAdmin):
    list_display = ['id', 'unique_number','sat_ssn','sat_ict', 'verdict']
    list_filter = ['unique_number',]
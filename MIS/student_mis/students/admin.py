from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('ReqNo', 'Name', 'Branch', 'Year', 'City', 'Country')
    search_fields = ('Name', 'Branch', 'City')

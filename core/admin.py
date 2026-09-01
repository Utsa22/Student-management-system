from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'email',
        'roll',
        'department',
        'owner',
        'created_at',
    )

    search_fields = (
        'name',
        'email',
        'department',
        'owner__username',
    )

    list_filter = (
        'department',
        'created_at',
    )

    ordering = (
        'roll',
    )
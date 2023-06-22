from django.contrib import admin

from .models import User, Event, Report, Question


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = [
        'username',
        'firstname',
        'role',
    ]
    list_display = [
        'username',
        'firstname',
        'role',
    ]
    list_filter = [
        'role',
    ]


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    search_fields = [
        'title',
    ]
    list_display = [
        'title',
        'date',
    ]


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    search_fields = [
        'title',
    ]
    list_display = [
        'title',
        'speaker',
        'event',
    ]
    list_filter = [
        'event',
    ]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    search_fields = [
        'question',
    ]
    list_display = [
        'question',
        'user',
        'report',
    ]
    list_filter = [
        'report__event',
        'report__speaker',
    ]

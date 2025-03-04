from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Textbook

#
# class StudentAdmin(UserAdmin):
#     """
#     Custom admin interface for the Student model.
#     Extends Django's built-in UserAdmin to include Concordia-specific fields.
#     """
#     list_display = ('concordia_id', 'email', 'first_name', 'last_name', 'is_staff')
#     search_fields = ('concordia_id', 'email', 'first_name', 'last_name')
#     fieldsets = (
#         ('Concordia Info', {'fields': ('concordia_id',)}),
#         ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
#         ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
#         ('Important Dates', {'fields': ('last_login', 'date_joined')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('concordia_id', 'email', 'first_name', 'last_name'),
#         }),
#     )
#
#
# class TextbookAdmin(admin.ModelAdmin):
#     """
#     Admin interface for the Textbook model.
#     """
#     list_display = ('title', 'author', 'edition', 'condition', 'course_code', 'owner', 'is_available')
#     list_filter = ('condition', 'is_available', 'course_code')
#     search_fields = ('title', 'author', 'course__code', 'owner__concordia_id')
#     readonly_fields = ('owner',)  # Prevent editing the owner directly in the admin panel
#
#
# admin.site.register(User, StudentAdmin)
# admin.site.register(Textbook, TextbookAdmin)
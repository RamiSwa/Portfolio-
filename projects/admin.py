from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget  # ✅ NEW

from .models import Project, ProjectImage, Technology


class ProjectAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())  # ✅ Apply rich editor

    class Meta:
        model = Project
        fields = '__all__'


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm  # ✅ Use custom form
    list_display = ('title', 'category', 'is_featured', 'date_created')
    list_editable = ('is_featured',)
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProjectImageInline]
    filter_horizontal = ('technologies',)
    search_fields = ('title', 'description', 'category')
    list_filter = ('category', 'technologies', 'is_featured', 'date_created')


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'link')
    search_fields = ('name',)

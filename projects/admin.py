from django.contrib import admin
from .models import Project, ProjectImage, Technology

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date_created')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProjectImageInline]
    filter_horizontal = ('technologies',)  # Better UI for ManyToMany in admin
    search_fields = ('title', 'description', 'category')
    list_filter = ('category', 'technologies', 'date_created')

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'link')
    search_fields = ('name',)

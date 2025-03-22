from django.contrib import admin
from .models import Project, ProjectImage, Technology

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_featured', 'date_created')  # ✅ Shows 'is_featured' in admin list
    list_editable = ('is_featured',)  # ✅ Allows toggling featured directly from the list view
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProjectImageInline]
    filter_horizontal = ('technologies',)  # ✅ Keeps the ManyToMany UI clean
    search_fields = ('title', 'description', 'category')
    list_filter = ('category', 'technologies', 'is_featured', 'date_created')  # ✅ Adds a filter for 'is_featured'

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'link')
    search_fields = ('name',)

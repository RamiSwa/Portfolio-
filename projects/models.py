from django.db import models
from django.utils.text import slugify

class Technology(models.Model):
    """Represents a single technology or tool (e.g., Django, Docker, PostgreSQL)."""
    name = models.CharField(max_length=100, unique=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    category = models.CharField(max_length=100)
    github_link = models.URLField(blank=True, null=True)
    demo_link = models.URLField(blank=True, null=True)
    date_created = models.DateField(auto_now_add=True)
    meta_description = models.CharField(max_length=160, blank=True)

    # ✅ NEW: ManyToMany with Technology
    technologies = models.ManyToManyField(Technology, related_name="projects", blank=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_created']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images/')

    def __str__(self):
        return f"Image for {self.project.title}"

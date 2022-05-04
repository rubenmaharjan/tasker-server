from django.contrib import admin
from .models import Project, Deliverable, SubDeliverable

# Register your models here.

admin.site.register(Project)
admin.site.register(Deliverable)
admin.site.register(SubDeliverable)

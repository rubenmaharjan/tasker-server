from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    duration = models.IntegerField()
    duration_type = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    class Meta:
       ordering = ['id']

    def __str__(self):
       return self.name

class Deliverable(models.Model):
    project = models.ForeignKey(Project, related_name='deliverables', on_delete=models.CASCADE, default=None)
    id = models.AutoField(primary_key=True)
    deliverable = models.CharField(max_length=100)

    class Meta:
       ordering = ['id']

    def __str__(self):
       return self.deliverable

class SubDeliverable(models.Model):
    deliverable = models.ForeignKey(Deliverable, related_name='sub_deliverables', on_delete=models.CASCADE, default=None)
    id = models.AutoField(primary_key=True)
    sub_deliverable = models.CharField(max_length=100)

    class Meta:
       ordering = ['id']

    def __str__(self):
       return self.sub_deliverable


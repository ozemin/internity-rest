from django.db import models
from uuid import uuid4

from companies.models import Company
from recruiters.models import Recruiter


class Job(models.Model):
    jobId = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    description = models.TextField()
    province = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    isActive = models.BooleanField(default=True)
    isDraft = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + " " + self.company.name

    class Meta:
        db_table = 'Jobs'
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'
        ordering = ['-createdAt']






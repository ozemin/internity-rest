from django.db import models
from recruiters.models import Recruiter

from uuid import uuid4

# Create your models here.


class Company(models.Model):
    companyId = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE, related_name='companies', db_column='recruiterId')
    logo = models.ImageField(upload_to='logos/', null=True, blank=True, default='logos/default.png')
    name = models.CharField(max_length=100)
    about = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    employees = models.IntegerField()
    established = models.IntegerField()
    isActive = models.BooleanField(default=False)
    isVerified = models.BooleanField(default=False)
    isPremium = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Companies'
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
        ordering = ['createdAt']





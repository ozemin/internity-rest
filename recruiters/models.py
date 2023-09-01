from django.db import models
from uuid import uuid4
from users.models import User


# Create your models here.
class Recruiter(models.Model):
    recruiterId = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='recruiter', db_column='userId')
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.email}'

    class Meta:
        db_table = 'Recruiters'
        verbose_name = 'Recruiter'
        verbose_name_plural = 'Recruiters'
        ordering = ['createdAt']



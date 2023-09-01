from django.db import models
from uuid import uuid4
from users.models import User


# Create your models here.
class Intern(models.Model):
    internId = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='intern', db_column='userId')
    photo = models.ImageField(upload_to='interns/', null=True, default='interns/default.jpg')
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, null=True)
    phone = models.CharField(max_length=20, null=True)
    birthDate = models.DateField(null=True)
    gender = models.CharField(max_length=6, null=True)
    isPremium = models.BooleanField(default=False)
    isVerified = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.email}'

    class Meta:
        db_table = 'Interns'
        verbose_name = 'Intern'
        verbose_name_plural = 'Interns'
        ordering = ['createdAt']

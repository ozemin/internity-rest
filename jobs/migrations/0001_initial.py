# Generated by Django 4.1 on 2023-09-03 13:36

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0002_alter_company_logo'),
        ('recruiters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('jobId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('province', models.CharField(max_length=100)),
                ('town', models.CharField(max_length=100)),
                ('isActive', models.BooleanField(default=True)),
                ('isDraft', models.BooleanField(default=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='companies.company')),
                ('recruiter', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='recruiters.recruiter')),
            ],
            options={
                'verbose_name': 'Job',
                'verbose_name_plural': 'Jobs',
                'db_table': 'Jobs',
                'ordering': ['-createdAt'],
            },
        ),
    ]

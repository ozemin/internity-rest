from rest_framework import serializers

from jobs.models import Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
        read_only_fields = ['jobId', 'createdAt', 'updatedAt', 'isActive', 'isDraft', 'recruiter', 'company']

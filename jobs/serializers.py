from rest_framework import serializers

from jobs.models import Job, JobApplication


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
        read_only_fields = ['jobId', 'createdAt', 'updatedAt', 'isActive', 'isDraft', 'recruiter', 'company']


class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = '__all__'
        read_only_fields = ['jobApplicationId', 'createdAt', 'updatedAt', 'job', 'intern', 'status']

    def validate(self, data):
        try:
            intern = self.context['request'].user.intern
        except:
            intern = None

        if intern is None:
            raise serializers.ValidationError("Sadece stajyerler başvuru yapabilir.")





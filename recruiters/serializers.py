from rest_framework import serializers
import datetime

from recruiters.models import Recruiter


class RecruiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruiter
        fields = ['recruiterId', 'firstName', 'lastName', 'phone', 'createdAt', 'updatedAt']
        read_only_fields = ['recruiterId', 'createdAt', 'updatedAt']

    def validate(self, data):
        if data['firstName'] == '':
            raise serializers.ValidationError('First name cannot be empty')
        if data['lastName'] == '':
            raise serializers.ValidationError('Last name cannot be empty')
        if data['phone'] == '':
            raise serializers.ValidationError('Phone cannot be empty')
        if data['phone'] != '':
            if len(data['phone']) != 10:
                raise serializers.ValidationError('Phone number should be of 10 digits')
            if not data['phone'].isdigit():
                raise serializers.ValidationError('Phone number should contain only digits')
        return data
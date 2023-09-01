from rest_framework import serializers

from companies.models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['logo', 'name', 'about', 'sector', 'website', 'employees',
                  'established', 'isVerified', 'isActive', 'isPremium',
                  'createdAt', 'updatedAt']
        read_only_fields = ['createdAt', 'updatedAt']

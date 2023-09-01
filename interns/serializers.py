from rest_framework import serializers
import datetime

from interns.models import Intern


class InternSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intern
        fields = ['firstName', 'lastName', 'email', 'phone', 'birthDate', 'gender']

    @staticmethod
    def validate_email(value):
        if Intern.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value

    @staticmethod
    def validate_phone(value):
        if Intern.objects.filter(phone=value).exists():
            raise serializers.ValidationError("Phone already exists")
        return value

    @staticmethod
    def validate_birthDate(value):
        if value > datetime.date.today():
            raise serializers.ValidationError("Birth date is not valid")
        return value

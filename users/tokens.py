from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers


User = get_user_model()


class TokenObtainPairSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = User.objects.filter(email=email).first()
        role = user.role


        if user is None:
            raise serializers.ValidationError("Kullanıcı bulunamadı")

        if not user.check_password(password):
            raise serializers.ValidationError("Parola hatalı")



        data = {}
        # refresh token with user and role
        refresh = RefreshToken.for_user(user)
        refresh['role'] = role
        refresh['maminin en yakin arkadasi'] = 'ömer'
        data['access'] = str(refresh.access_token)
        data['refresh'] = str(refresh)

        return data
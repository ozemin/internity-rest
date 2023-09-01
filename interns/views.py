from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny

from users.models import User
from interns.models import Intern

from users.serializers import UserSerializer
from interns.serializers import InternSerializer

from users.tokens import TokenObtainPairSerializer

from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.


class InternRegister(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    @staticmethod
    def post(request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            user = User.objects.create_user(**serializer.validated_data)
            user.role = 'intern'
            user.isActive = True
            user.isVerified = True

            user.save()

            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class InternLogin(APIView):
    @staticmethod
    def post(request, *args, **kwargs):
        serializer = TokenObtainPairSerializer(data=request.data)

        if serializer.is_valid():
            return Response(serializer.validated_data, status=200)

        return Response(serializer.errors, status=400)


class InternProfileRegister(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    @staticmethod
    def post(request, *args, **kwargs):
        serializer = InternSerializer(data=request.data)

        if serializer.is_valid():
            intern = Intern.objects.create(**serializer.validated_data, user=request.user)
            intern.save()

            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class InternProfile(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    @staticmethod
    def get(request, *args, **kwargs):
        intern = Intern.objects.get(user=request.user)
        serializer = InternSerializer(intern)

        return Response(serializer.data, status=200)

    @staticmethod
    def put(request, *args, **kwargs):
        intern = Intern.objects.get(user=request.user)
        serializer = InternSerializer(intern, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


class InternLogout(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    @staticmethod
    def post(request, *args, **kwargs):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({'message': 'You have been logged out'}, status=200)
        except Exception as e:
            return Response(status=400)
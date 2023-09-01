from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny




from users.models import User
from recruiters.models import Recruiter

from users.serializers import UserSerializer
from recruiters.serializers import RecruiterSerializer

from users.tokens import TokenObtainPairSerializer

# Create your views here.


class RecruiterRegister(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    @staticmethod
    def post(request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            user = User.objects.create_user(**serializer.validated_data)
            user.role = 'recruiter'
            user.isActive = True
            user.isVerified = True

            user.save()

            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class RecruiterLogin(APIView):
    @staticmethod
    def post(request, *args, **kwargs):
        serializer = TokenObtainPairSerializer(data=request.data)

        if serializer.is_valid():
            return Response(serializer.validated_data, status=200)

        return Response(serializer.errors, status=400)


class RecruiterProfileRegister(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    @staticmethod
    def post(request, *args, **kwargs):
        serializer = RecruiterSerializer(data=request.data)

        if serializer.is_valid():
            recruiter = Recruiter.objects.create(**serializer.validated_data, user=request.user)
            recruiter.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class RecruiterProfile(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    @staticmethod
    def get(request, *args, **kwargs):
        recruiter = request.user.recruiter
        serializer = RecruiterSerializer(recruiter)
        return Response(serializer.data, status=200)

    @staticmethod
    def put(request, *args, **kwargs):
        recruiter = request.user.recruiter
        serializer = RecruiterSerializer(recruiter, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


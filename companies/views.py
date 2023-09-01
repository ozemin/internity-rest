from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny

from users.models import User
from recruiters.models import Recruiter
from companies.models import Company

from companies.serializers import CompanySerializer


# Create your views here.


class CompanyRegister(APIView):
    permission_classes = [AllowAny]
    authentication_classes = [JWTAuthentication]

    @staticmethod
    def post(request, *args, **kwargs):
        serializer = CompanySerializer(data=request.data)

        if Company.objects.filter(recruiter=request.user.recruiter).exists():
            return Response({'error': 'You have already created a company'}, status=400)

        if serializer.is_valid():
            serializer.save(recruiter=request.user.recruiter)

            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class CompanyProfile(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    @staticmethod
    def get(request, *args, **kwargs):
        try:
            company = Company.objects.get(recruiter=request.user.recruiter)
            serializer = CompanySerializer(company)
            return Response(serializer.data, status=200)
        except Company.DoesNotExist:
            return Response({'error': 'You have not created a company yet'}, status=400)

    @staticmethod
    def put(request, *args, **kwargs):
        try:
            company = Company.objects.get(recruiter=request.user.recruiter)
            serializer = CompanySerializer(company, data=request.data)

            if serializer.is_valid():
                serializer.save(recruiter=request.user.recruiter)
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=400)
        except Company.DoesNotExist:
            return Response({'error': 'You have not created a company yet'}, status=400)

from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny

from jobs.models import Job

from jobs.serializers import JobSerializer


class JobCreate(APIView):
    permission_classes = [AllowAny]
    authentication_classes = [JWTAuthentication]

    @staticmethod
    def post(request):
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid() and request.user.recruiter:
            recruiter = request.user.recruiter
            company = recruiter.companies.first()
            serializer.save(recruiter=recruiter, company=company)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=422)


class JobDetail(APIView):
    permission_classes = [AllowAny]
    authentication_classes = [JWTAuthentication]

    @staticmethod
    def get(request, pk):
        job = Job.objects.get(pk=pk)
        serializer = JobSerializer(job)
        return Response(serializer.data, status=200)

    @staticmethod
    def put(request, pk):
        job = Job.objects.get(pk=pk)
        recruiter = request.user.recruiter
        company = recruiter.companies.first()
        serializer = JobSerializer(job, data=request.data)
        if serializer.is_valid() and request.user.recruiter and job.recruiter == recruiter and job.company == company:
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=422)

    @staticmethod
    def delete(request, pk):
        job = Job.objects.get(pk=pk)
        job.delete()
        return Response(status=204)


class JobList(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    @staticmethod
    def get(request):
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data, status=200)
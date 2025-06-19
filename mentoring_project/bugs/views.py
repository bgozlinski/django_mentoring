from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import generics
from .serializers import BugSerializer
from .models import Bug
from projects.models import Project
from django.contrib.auth.models import User


class GetAllBugs(generics.ListAPIView):
    serializer_class = BugSerializer
    queryset = Bug.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({'bugs': serializer.data})

@api_view()
def bugs_view(request):
    project_id = request.query_params.get('project_id')
    user_id = request.query_params.get('user_id')

    if not project_id and not user_id:
        return Response({'error': 'project_id or user_id is required'},
                        status=status.HTTP_400_BAD_REQUEST)

    queryset = Bug.objects.all()

    if project_id:
        try:
            project = Project.objects.get(id=project_id)
            queryset = queryset.filter(project=project)
        except Project.DoesNotExist:
            return Response(
                {"error": f"Project with id {project_id} does not exist"},
                status=status.HTTP_404_NOT_FOUND
            )

    if user_id:
        try:
            user = User.objects.get(id=user_id)
            queryset = queryset.filter(user=user)
        except User.DoesNotExist:
            return Response(
                {"error": f"User with id {user_id} does not exist"},
                status=status.HTTP_404_NOT_FOUND
            )

    serializer = BugSerializer(queryset, many=True)

    return Response({'bugs': serializer.data}, status=status.HTTP_200_OK)

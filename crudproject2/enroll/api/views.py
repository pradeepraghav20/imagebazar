from enroll.api.serializers import StudentSerializers
from enroll.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.authentication import BasicAuthentication,SessionAuthentication

class StudentViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=StudentSerializers
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]



from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import response
from rest_framework.status import HTTP_204_NO_CONTENT

from .models import CreateNewLead
from .serializers import CreateNewLeadSerializer
# Create your views here.

class CreateNewLeadViewSet(viewsets.ModelViewSet):

    queryset = CreateNewLead.objects.all()
    serializer_class = CreateNewLeadSerializer

    def destroy(self, request, pk=None):
        
        instance = self.get_object()
        instance.delete()

        return response.Response({'messsage':"Record delete successfully"},status=HTTP_204_NO_CONTENT)
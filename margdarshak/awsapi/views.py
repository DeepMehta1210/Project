from rest_framework import generics, status
from rest_framework.response import Response
from .models import Zone, Area, Cluster, WLSU, Cedative
from .serializers import ZoneSerializer, AreaSerializer, ClusterSerializer, WLSUSerializer, CedativeSerializer

class ZoneListCreate(generics.ListCreateAPIView):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer

class ZoneRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer

class AreaListCreate(generics.ListCreateAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

class AreaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

class ClusterListCreate(generics.ListCreateAPIView):
    queryset = Cluster.objects.all()
    serializer_class = ClusterSerializer

class ClusterRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cluster.objects.all()
    serializer_class = ClusterSerializer

class WLSUListCreate(generics.ListCreateAPIView):
    queryset = WLSU.objects.all()
    serializer_class = WLSUSerializer

class WLSURetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = WLSU.objects.all()
    serializer_class = WLSUSerializer

class CedativeListCreate(generics.ListCreateAPIView):
    queryset = Cedative.objects.all()
    serializer_class = CedativeSerializer

class CedativeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cedative.objects.all()
    serializer_class = CedativeSerializer

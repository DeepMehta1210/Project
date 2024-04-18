from rest_framework import generics, status
from rest_framework.response import Response
from .models import Zone, Area, Cluster, WLSU, Cedative
from .serializers import ZoneSerializer, AreaSerializer, ClusterSerializer, WLSUSerializer, CedativeSerializer
from django.http import JsonResponse
from .models import WLSU
import json

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


def get_water_level_data(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from request body
            data = json.loads(request.body.decode('utf-8'))

            # Extract turning points from JSON
            turning_points = data.get('turning_points', [])

            # Initialize list to store water level data for each segment
            segmented_water_level_data = []

            # Iterate over turning points
            for i in range(len(turning_points) - 1):
                # Extract latitude and longitude for each segment
                latitude_start = turning_points[i].get('latitude')
                longitude_start = turning_points[i].get('longitude')
                latitude_end = turning_points[i+1].get('latitude')
                longitude_end = turning_points[i+1].get('longitude')

                # Query WLSU model to get water level sensor data for the segment
                water_level_data = WLSU.objects.filter(
                    l1n1__lte=latitude_end,
                    l2n2__gte=latitude_start
                    # Assuming l1n1 and l2n2 are fields representing latitude range in the WLSU model
                    # Adjust the query based on your specific model structure
                ).filter(
                    # Add additional filters based on longitude range or other criteria if needed
                )

                # Serialize the data into JSON format for the segment
                serialized_data = [{
                    'wlsu_id': wlsu.wlsu_id,
                    'wlsu_name': wlsu.wlsu_name,
                    'water_level': wlsu.wll,
                    # Include other relevant fields from the WLSU model
                } for wlsu in water_level_data]

                # Append water level data for the segment to the segmented data list
                segmented_water_level_data.append({
                    'segment': f'{i+1} to {i+2}',
                    'water_level_data': serialized_data
                })

            # Return JSON response with segmented water level data
            return JsonResponse({'segmented_water_level_data': segmented_water_level_data})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)  
    elif request.method == 'GET':
        return JsonResponse({'message': 'This endpoint supports POST requests only'}, status=405)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
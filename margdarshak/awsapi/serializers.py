from rest_framework import serializers
from .models import Zone, Area, Cluster, WLSU, Cedative

class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = '__all__'

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'

class ClusterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cluster
        fields = '__all__'

class WLSUSerializer(serializers.ModelSerializer):
    class Meta:
        model = WLSU
        fields = '__all__'

class CedativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cedative
        fields = '__all__'

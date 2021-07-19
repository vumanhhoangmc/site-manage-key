from rest_framework import serializers
from .models import Managekey

class ResponseKey(serializers.ModelSerializer):
    class Meta:
        model = Managekey
        fields = ('key', 'tool', 'hsd',)

class SendDataKey(serializers.Serializer):
    keytool = serializers.CharField(max_length=200)      
    tool = serializers.CharField(max_length=200)

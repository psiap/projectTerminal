from rest_framework import serializers
from .models import *



class WcapiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = ('user_id', 'total_received', 'number_of_transactions')
from rest_framework import serializers
from .models import Roomate, Team, Transaction

class RoomateSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	class Meta:
		model = Roomate
		fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
        

class TransactionSerializer(serializers.ModelSerializer):

    user_name = serializers.SerializerMethodField()

    class Meta:
        model = Transaction
        fields = '__all__'
    
    def get_user_name(self,instance):
         return instance.user.user_id
    
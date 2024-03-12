from django.shortcuts import render
from rest_framework import viewsets,status
from .models import Roomate,Team,Transaction
from .serializers import RoomateSerializer,TeamSerializer,TransactionSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .permissions import IsAuthenticatedAndTokenValid,IsAuthenticatedAndTeamValid
from rest_framework.decorators import action


# Create your views here.
class RoomateViewSet(viewsets.ModelViewSet):
    serializer_class = RoomateSerializer
    queryset= Roomate.objects.all()

    # def get_queryset(self):
    #     pk=self.request.user.id
    #     print(self.request.user.id)
    #     return Roomate.objects.filter(id=pk)
    
    def retrieve(self, request, *args, **kwargs):
        id = kwargs['pk']
        try:
            roomate = Roomate.objects.get(id=id,token=request.headers.get('token'))
        except:
            return Response('Not Allowed to view this token',status=status.HTTP_403_FORBIDDEN)
        serializer = RoomateSerializer(roomate)
        return Response(serializer.data)
        

    def list(self, request, *args, **kwargs):
        return Response('Method not allowed',status=status.HTTP_403_FORBIDDEN)
    
    def get_permissions(self):
        if self.action == 'retrieve':
            return [IsAuthenticatedAndTokenValid()]
        else:
            return [AllowAny()]
    
    def destroy(self, request, *args, **kwargs):
        return Response('Method not allowed',status=status.HTTP_403_FORBIDDEN)
    
    def partial_update(self, request, *args, **kwargs):
        return Response('Method not allowed',status=status.HTTP_403_FORBIDDEN)
    
    def update(self, request, *args, **kwargs):
        return Response('Method not allowed',status=status.HTTP_403_FORBIDDEN)
    
    def login(self,request):
        user_id=request.data.get('user_id',None)
        password = request.data.get('password',None)
        if not user_id or not password:
            return Response('User Id or Password field is missing',status=status.HTTP_400_BAD_REQUEST)
        try:
            user = Roomate.objects.get(user_id=user_id,password=password)
        except:
            return Response('User ID or Password is incorrect',status=status.HTTP_400_BAD_REQUEST)
        serializer = RoomateSerializer(user)
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
    

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticatedAndTokenValid]

    def list(self, request, *args, **kwargs):
        if not request.user:
            return Response('User is not authenticated', status=status.HTTP_401_UNAUTHORIZED)
        user_id = request.user.id

        # list of teams where user is present
        team_list = Team.objects.filter(user_id=user_id)
        serializer = TeamSerializer(team_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        if not request.user:
            return Response('User is not authenticated', status=status.HTTP_401_UNAUTHORIZED)
        user_id = request.user.id
        id = kwargs['pk']
        try:
            team_list = Team.objects.get(user_id=user_id,id=id)
        except:
            return Response('Not Allowed to view this team',status=status.HTTP_403_FORBIDDEN)
        serializer = TeamSerializer(team_list)
        return Response(serializer.data)
        
    
    def create(self, request, *args, **kwargs):
        # Ensure the user is authenticated and token is valid
        if not request.user:
            return Response('User is not authenticated', status=status.HTTP_401_UNAUTHORIZED)

        team_id = request.data.get('team_id')
        team_name = request.data.get('team_name')

        # If both team_id and team_name are provided, try to join the team
        if team_id:
            try:
                team = Team.objects.get(team_id=team_id)
            except:
                return Response('Team does not exist.', status=status.HTTP_404_NOT_FOUND)

            user = request.user.id
            team.user_id.add(user)

            serializer = TeamSerializer(team, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # If team_id and team_name are not provided, create a new team
        elif team_name:
            user_id = request.user.id
            request.data['user_id'] = [user_id]
            return super().create(request, *args, **kwargs)

        # If only one of team_id or team_name is provided, return bad request
        else:
            return Response('Either Team ID or Team Name are required.', status=status.HTTP_400_BAD_REQUEST)
        
    
    def partial_update(self, request, *args, **kwargs):
        return Response('Method not allowed',status=status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        return Response('Method not allowed',status=status.HTTP_403_FORBIDDEN)
    

    def destroy(self, request, *args, **kwargs):
        if not request.user:
            return Response('User is not authenticated', status=status.HTTP_401_UNAUTHORIZED)
        user_id = request.user.id
        id = kwargs['pk']
        try:
            team = Team.objects.get(user_id=user_id,id=id)
        except:
            return Response('Not Allowed to delete this team',status=status.HTTP_403_FORBIDDEN)
        team.user_id.remove(user_id)
        return Response('Team deleted successfully', status=status.HTTP_204_NO_CONTENT)

    
        
class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticatedAndTeamValid]

    def create(self, request, *args, **kwargs):
        if not request.user:
            return Response('User is not authenticated', status=status.HTTP_401_UNAUTHORIZED)     
        team = request.data.get('team_id')
        user = request.user.id
        request.data['user'] = user 
        request.data['team']=team   
        return super().create(request, *args, **kwargs)

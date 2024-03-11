# basic URL Configurations
from django.urls import  path,include
from . import views
from rest_framework.routers import DefaultRouter

Router = DefaultRouter()

Router.register(r'user',views.RoomateViewSet)
Router.register(r'team',views.TeamViewSet)
Router.register(r'transaction',views.TransactionViewSet)

# specify URL Path for rest_framework
urlpatterns = [
	path('',include(Router.urls)),
    path('login',views.RoomateViewSet.as_view({'post':'login'})),
    # path('team/join_team/', views.TeamViewSet.join_team, name='team-join')
]

from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from .models import UserProfile, ActivityLog, Team, LeaderboardEntry
from .serializers import (
    UserSerializer,
    UserProfileSerializer,
    ActivityLogSerializer,
    TeamSerializer,
    LeaderboardEntrySerializer,
)

# User ViewSet (read-only)
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# UserProfile ViewSet
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# ActivityLog ViewSet
class ActivityLogViewSet(viewsets.ModelViewSet):
    queryset = ActivityLog.objects.all().order_by('-date')
    serializer_class = ActivityLogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Team ViewSet
class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Leaderboard ViewSet
class LeaderboardEntryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = LeaderboardEntry.objects.order_by('-points')
    serializer_class = LeaderboardEntrySerializer
    permission_classes = [permissions.AllowAny]

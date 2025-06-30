from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, ActivityLog, Team, LeaderboardEntry

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = UserProfile
        fields = ["user", "bio", "avatar", "team", "points"]

class ActivityLogSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = ActivityLog
        fields = ["id", "user", "activity_type", "duration_minutes", "distance_km", "date", "points_earned"]

class TeamSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Team
        fields = ["id", "name", "members", "total_points"]

class LeaderboardEntrySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = LeaderboardEntry
        fields = ["user", "points"]

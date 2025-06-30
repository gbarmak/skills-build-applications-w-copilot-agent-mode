# OctoFit Tracker Models
from djongo import models
from django.contrib.auth.models import User

# User profile with extra fields
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.URLField(blank=True)
    team = models.CharField(max_length=100, blank=True)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

# Activity log for fitness tracking
class ActivityLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=50)  # e.g., running, walking, strength
    duration_minutes = models.PositiveIntegerField()
    distance_km = models.FloatField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    points_earned = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.activity_type} on {self.date.date()}"

# Team model for group competitions
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    members = models.ManyToManyField(User, related_name='teams')
    total_points = models.IntegerField(default=0)

    def __str__(self):
        return self.name

# Leaderboard entry (denormalized for fast access)
class LeaderboardEntry(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}: {self.points} pts"

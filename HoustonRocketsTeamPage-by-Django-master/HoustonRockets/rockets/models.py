from django.db import models
import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


colors = {
    "Red": "R", "Silver": "S", 'Black': 'B',
    'White': "W"
}

COLOR_CHOICES = [(code, label) for label, code in colors.items()]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to="user_imgs", blank=True)
    def __str__(self):
        return "{} - {}".format(self.user.username, self.id)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Comment(models.Model):
    title = models.CharField(max_length=150, blank=True)
    body = models.TextField(blank=True)
    player = models.ForeignKey('Player', on_delete=models.CASCADE, blank=True)
    user1 = models.ForeignKey(User, on_delete=models.CASCADE,null=True)


class Player(models.Model):
    name = models.CharField(max_length=80)
    biography = models.TextField(blank=True)
    age = models.IntegerField(blank=True)
    image = models.ImageField(upload_to="imgs", blank=True)
    height = models.FloatField(default=20,blank=True)
    weight = models.FloatField(default=20,blank=True)
    birthplace = models.CharField(max_length=80,blank=True)
    previously = models.TextField(blank=True)
    nba_debut = models.IntegerField(default=20,blank=True)
    years_in_nba = models.IntegerField(default=20,blank=True)
    position = models.CharField(max_length=80)
    number = models.IntegerField(default=20, blank=True)
    games_played = models.IntegerField(default=20, blank=True)
    field_goals_made = models.FloatField(default=20, blank=True)
    points = models.FloatField(default=20, blank=True)
    field_goal = models.FloatField(default=20, blank=True)
    three_points = models.FloatField(default=20, blank=True)
    free_throw = models.FloatField(default=20, blank=True)
    offensive_rebounds = models.FloatField(default=20, blank=True)
    deffensive_rebounds = models.FloatField(default=20,blank=True)
    rebounds = models.FloatField(default=20,blank=True)
    assists = models.FloatField(default=20, blank=True)
    steals = models.FloatField(default=20, blank=True)
    turn_overs = models.FloatField(default=20, blank=True)
    fouls = models.FloatField(default=20, blank=True)


    def __str__(self):
        return "{} - {}".format(self.name, self.number)


class Player_Gallery(models.Model):
    image = models.ImageField(upload_to="player_photos", blank=True)
    player = models.ForeignKey('Player',  blank=True,on_delete=models.CASCADE)


class Match(models.Model):
    name = models.CharField(max_length=80)
    video = models.CharField(max_length=300,default="kNst9WrrJRA")
    start_day = models.DateField(default=datetime.date.today)
    start_time = models.TimeField(default=datetime.datetime.now)
    arena = models.CharField(max_length=80,default="Texas",blank=True)
    lat = models.FloatField(default=29.751003, blank=True)
    lng = models.FloatField(default=-95.362122, blank=True)
    vs = models.ImageField(upload_to="imgs", blank=True)
    score = models.CharField(max_length=80, blank=True)
    price = models.FloatField(blank=True)
    seating_map = models.ImageField(upload_to="imgs", blank=True)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=80)
    conference = models.CharField(max_length=80)
    division = models.CharField(max_length=80)
    founded = models.IntegerField(default=20,blank=True)
    history = models.TextField(blank=True)
    arena = models.CharField(max_length=80,blank=True)
    location = models.CharField(max_length=80,blank=True)
    team_colors = models.CharField(max_length=200, choices=COLOR_CHOICES)
    general_manager = models.CharField(max_length=80,blank=True)
    head_coach = models.CharField(max_length=80,blank=True)
    ownership = models.CharField(max_length=80,blank=True)
    championships = models.IntegerField(default=20,blank=True)
    uniforms = models.ImageField(upload_to="imgs", blank=True)


class Ticket(models.Model):
    seat_number = models.IntegerField(default=20,blank=True)
    creditcard = models.CharField(max_length=80,blank=True)
    match = models.ForeignKey('Match', on_delete=models.CASCADE, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)















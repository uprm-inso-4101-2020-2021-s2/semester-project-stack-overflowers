from django.contrib.postgres.fields import JSONField
from django.db import models
from social_django import models as oauth_models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class PlayerAccount(models.Model):
    player_name = models.CharField(max_length=128)
    user_name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.user_name


class Image_Model(models.Model):
    img_id = models.IntegerField(primary_key=True)
    img_url = models.URLField(max_length=200)


class Game_Model(models.Model):
    game_id = models.IntegerField(primary_key=True)
    game_title = models.CharField(max_length=128)
    genres = JSONField()
    developers = JSONField()
    platforms = JSONField()
    img_id = models.ForeignKey(Image_Model, on_delete=models.CASCADE)


class Library_Model(models.Model):
    owner_id = models.ForeignKey(oauth_models.USER_MODEL, on_delete=models.CASCADE)
    games = models.ManyToManyField(Game_Model, through='Library_Membership')


class Library_Membership(models.Model):
    game = models.ForeignKey(Game_Model, on_delete=models.CASCADE)
    library = models.ForeignKey(Library_Model, on_delete=models.CASCADE)
    last_played = models.DateField()
    is_finished = models.BooleanField(default=False)
    forced_to_backlog = models.BooleanField(default=False)


class Ratings_Model(models.Model):
    game = models.ForeignKey(Game_Model, on_delete=models.CASCADE)
    user_id = models.ForeignKey(oauth_models.USER_MODEL, on_delete=models.CASCADE)
    overall_rating = models.IntegerField(primary_key=False)

    class Meta:
        db_table = "index_ratings_model"

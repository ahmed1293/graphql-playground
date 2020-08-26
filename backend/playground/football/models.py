from django.db import models



class Competition(models.Model):
    KNOCKOUT = 0
    LEAGUE = 1
    FORMAT_CHOICES = [
        (KNOCKOUT, 'Knockout'),
        (LEAGUE, 'League')
    ]
    
    name = models.CharField(max_length=30)
    format = models.PositiveSmallIntegerField(
        choices=FORMAT_CHOICES
    )


class Team(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    competitions = models.ManyToManyField(Competition)



class Manager(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.PositiveSmallIntegerField()
    team = models.OneToOneField(
        Team, 
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )


class Player(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.PositiveSmallIntegerField()
    age = models.PositiveSmallIntegerField()
    team = models.ForeignKey(
        Team, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )


class Stadium(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    capacity = models.PositiveIntegerField()
    team = models.ForeignKey(
        Team, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )
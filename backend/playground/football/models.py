from django.db import models


class Manager(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Stadium(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    manager = models.OneToOneField(
        Manager, on_delete=models.SET_NULL, null=True, blank=True
    )
    stadium = models.ForeignKey(
        Stadium, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.name


class Competition(models.Model):
    KNOCKOUT = 0
    LEAGUE = 1
    FORMAT_CHOICES = [(KNOCKOUT, "Knockout"), (LEAGUE, "League")]

    name = models.CharField(max_length=30)
    format = models.PositiveSmallIntegerField(choices=FORMAT_CHOICES)
    teams = models.ManyToManyField(Team)

    def __str__(self):
        return self.name


class Player(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.PositiveSmallIntegerField()
    age = models.PositiveSmallIntegerField()
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

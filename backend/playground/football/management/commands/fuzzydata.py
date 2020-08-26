from django.core.management.base import BaseCommand
from football.factories import (
    CompetitionFactory,
    TeamFactory,
    ManagerFactory,
    PlayerFactory,
    StadiumFactory,
)
from football.models import Competition, Team, Manager, Player, Stadium


class Command(BaseCommand):
    help = "Generate a bunch of random model data"

    def handle(self, *args, **options):
        self.stdout.write("Creating teams")
        teams = [TeamFactory() for _ in range(0, 20)]

        self.stdout.write("Creating competitions")
        for _ in range(0, 5):
            CompetitionFactory(teams=teams)

        self.stdout.write("Creating players")
        for team in teams:
            for _ in range(0, 23):
                PlayerFactory(team=team)

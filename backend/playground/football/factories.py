from factory import fuzzy, post_generation, django, SubFactory
from football.models import Competition, Team, Manager, Player, Stadium


class CompetitionFactory(django.DjangoModelFactory):
    class Meta:
        model = Competition

    name = fuzzy.FuzzyText()
    format = fuzzy.FuzzyChoice([Competition.KNOCKOUT, Competition.LEAGUE])

    @post_generation
    def teams(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for team in extracted:
                self.teams.add(team)


class StadiumFactory(django.DjangoModelFactory):
    class Meta:
        model = Stadium

    name = fuzzy.FuzzyText()
    city = fuzzy.FuzzyText()
    capacity = fuzzy.FuzzyInteger(10000, 90000)


class ManagerFactory(django.DjangoModelFactory):
    class Meta:
        model = Manager

    first_name = fuzzy.FuzzyText()
    last_name = fuzzy.FuzzyText()
    age = fuzzy.FuzzyInteger(18, 90)


class TeamFactory(django.DjangoModelFactory):
    class Meta:
        model = Team

    name = fuzzy.FuzzyText()
    country = fuzzy.FuzzyText()
    manager = SubFactory(ManagerFactory)
    stadium = SubFactory(StadiumFactory)


class PlayerFactory(django.DjangoModelFactory):
    class Meta:
        model = Player

    first_name = fuzzy.FuzzyText()
    last_name = fuzzy.FuzzyText()
    number = fuzzy.FuzzyInteger(1, 150)
    age = fuzzy.FuzzyInteger(18, 90)
    team = SubFactory(TeamFactory)

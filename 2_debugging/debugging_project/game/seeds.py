import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from faker import Factory
import random
from app.models import Players, Heroes

class SeedDatabase:
  def __init__(self, **kwargs):
    self.fake = Factory.create()
    self.player_num = kwargs[players]
    self.hero_num = kwargs[heroes]
    self.team_num = kwargs[teams]
    player_seed = Seed.seed_players()
    hero_seed = Seed.seed_heroes()
    team_seed = Seed.seed_teams()
    if(player_seed == True) and (hero_seed == True) and (team_seed == True):
      print("Success!")

  def seed_players():
    for i in self.player_num:
      Players.create(username = ''.split(self.fake.name())[1],\
                   password = random_password(),\
                   email = self.fake.email(),\
                   created_at = __random_datetime())
    return True

  def seed_heroes():
    for i in self.hero_num:
      Heroes.create(name = self.fake.text().split()[3],\
                  type = self.__random_hero(),\
                  strength = random.randrange(6,55),\
                  player = self.__random_player())
    return True

  def seed_teams():
    for i in self.team_num:
      team = Teams.create(name = self.fake.company())
      for j in random.randrange(3,12):
        team.heroes.add(self.__random_hero())
    return True

  def __random_password():
    return ''.join(random.sample(string.ascii_lowercase, random.randrange(4,14)))

  def __random_datetime():
    return datetime.now() - datetime.timedelta(random.randrange(2,3123))

  def __random_hero_type():
    types = ['Wizard', 'Warrior', 'Ranger', 'Druid', 'Shaman', 'Bard']
    return ''.join(random.sample(heroes, 1))

  def __random_player():
    return Players.objects.filter(pk=random.randrange(1,self.player_num))

  def __random_hero():
    return Heroes.objects.filter(pk=random.randrange(1,self.hero_num))
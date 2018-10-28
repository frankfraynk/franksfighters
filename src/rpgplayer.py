class Player: #Create a class for the player with different attributes
    def __init__(self, name):
        self.name = name
        self.maxhealth = 1001
        self.health = self.maxhealth
        self.armor = 4
        self.attacks = []
        self.gold = 100
        self.pots = 0
        self.speed = 4

health_dashes = 20
def player_health(player):
  dash_convert = int(player.maxhealth/health_dashes)
  current_dashes = int(player.health/dash_convert)
  remaining_health = health_dashes - current_dashes

  health_display = ''.join(['-' for i in range(current_dashes)])
  remaining_display = ''.join([' ' for i in range(remaining_health)])
  percent = str(int((player.health/player.maxhealth)*100)) + "%"

  print("|" + health_display + remaining_display + "|")
  print("         " + percent)

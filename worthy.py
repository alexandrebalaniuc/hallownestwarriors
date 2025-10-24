import warrior

warrior_one = warrior.Warrior("Knight", 150, 20)
warrior_one.name = "Knight"
warrior_one.power = 150
warrior_one.weapon = 20

warrior2 = warrior.Warrior("Hornet", 120, 150)
warrior2.name = "Hornet"
warrior2.power = 120
warrior2.weapon = 150

warrior3 = warrior.Warrior("Hollow Knight", 145, 145)
warrior3.name = "Hollow Knight"
warrior3.power = 145
warrior3.weapon = 145

warrior4 = warrior.Warrior("Watcher Knights", 60, 70)
warrior4.name = "Watcher Knights"
warrior4.power = 60
warrior4.weapon = 70
print(warrior_one.worthy())
print(warrior2.worthy())
print(warrior3.worthy())
print(warrior4.worthy())
print(warrior_one.surge())
print(warrior2.surge())
print(warrior3.dishonor())

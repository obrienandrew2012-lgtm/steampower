import random
import sys

gold = 0
player_hp = 30
relic = 0

print("HELLO DUNGEON CRAWLER!")
answer = input("ARE YOU READY TO GO IN THE DUNGEON??? Y/N ").upper()

if answer == "N":
    input("ok bye, hit enter to leave")
    sys.exit()

print("*hear that?*")
print("*eyes glow in the dark*")

creatures = ["Goblin", "Slime", "Skeleton", "Bat", "Tiny Demon"]
creature = random.choice(creatures)
creature_hp = random.randint(8, 15)

print(f"\nA {creature} appears!")
choice = input("FIGHT, CHECK THEIR STATS, OR RUN? F/C/R ").upper()

if choice == "C":
    print(f"{creature} HP: {creature_hp}")
    print("Damage per hit: 3–8")
    choice = input("Now what? FIGHT OR RUN? F/R ").upper()

if choice == "R":
    print("You run away safely...")
    sys.exit()

if choice == "F":
    print(f"\nYou engage the {creature}!")
    while player_hp > 0 and creature_hp > 0:
        player_damage = random.randint(6, 12)
        creature_hp -= player_damage
        print(f"You hit the {creature} for {player_damage} damage!")

        if creature_hp <= 0:
            gold += 10
            relic = 1
            print(f"The {creature} is defeated!")
            print("You gained 10 GOLD")
            break

        creature_damage = random.randint(3, 8)
        player_hp -= creature_damage
        print(f"The {creature} hits you for {creature_damage} damage!")
        print(f"Your HP: {player_hp}")

        if player_hp <= 0:
            print("You collapse... GAME OVER")
            sys.exit()

print("\nYou move deeper into the dungeon...")
action = input("What to do now? S(hop), W(all), E(xplore): ").upper()
print(action)

if action == "E" and relic == 1:
    print("\nKermit appears...")
    kermit_hp = 9000000000000000000
    first_hit = True

    while player_hp > 0 and kermit_hp > 0:
        kermit_hp -= 1
        print("You hit Kermit for 1 damage!")
        print(f"Kermit HP: {kermit_hp}")

        if kermit_hp <= 0:
            print("Kermit has been defeated!")
            break

        if first_hit:
            player_hp -= 1
            print("Kermit spares you... He hits you for 1 damage.")
            print(f"Your HP: {player_hp}")
            first_hit = False
        else:
            player_hp -= 9000000000000000000000000000
            print("Kermit unleashes true power...")
            print("He hits you for 9 octillion damage!")
            print(f"Your HP: {player_hp}")

        if player_hp <= 0:
            print("You have been obliterated... GAME OVER")
            sys.exit()

print(f"\nYou survive with {player_hp} HP and {gold} GOLD!")

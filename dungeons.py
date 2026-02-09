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

if action == "W":
    print("You find strange writings on the wall...")
    input("All you can read is: '✈︎🕈︎☜︎☼︎❄︎☪︎ 💧︎❄︎🕆︎👎︎✋︎⚐︎ ☝︎✌︎💣︎☜︎💧︎'")

if action == "S":
    print("Welcome to the Shop!")
    buy1 = input("Buy H(eal), B(etter Sword), or K(ermit Relic)? ").upper()

    if buy1 == "H" and gold >= 5:
        gold -= 5
        player_hp += 5
        print("You healed 5 HP")

    elif buy1 == "B":
        print("You got the Better Sword (it looks cool)")

    elif buy1 == "K":
        print("you got the KERMIT RELIC")
        relic = 1

    else:
        print("You leave the shop")

if action == "E":
    print("\n*The ground shakes...*")

    strong_monsters = ["Orc", "Troll", "Rock Monster", "Giant Spider"]
    strong = random.choice(strong_monsters)
    strong_hp = random.randint(20, 35)

    print(f"A {strong} appears!")

    if input("FIGHT OR RUN? F/R ").upper() == "R":
        print("You barely escape...")
        sys.exit()

    print(f"You fight the {strong}!")

    while player_hp > 0 and strong_hp > 0:
        player_damage = random.randint(8, 15)
        strong_hp -= player_damage
        print(f"You strike the {strong} for {player_damage} damage!")

        if strong_hp <= 0:
            gold += 25
            print(f"You defeated the {strong}!")
            print("You gained 25 GOLD")
            break

        strong_damage = random.randint(6, 12)
        player_hp -= strong_damage
        print(f"The {strong} smashes you for {strong_damage} damage!")
        print(f"Your HP: {player_hp}")

        if player_hp <= 0:
            print("The dungeon claims another victim...")
            sys.exit()

print(f"\nYou survive with {player_hp} HP and {gold} GOLD!")

# 🐸 KERMIT EVENT
if action == "E" and relic == 1:
    print("IS THAT KERMIT THE FROG")
    print("*KERMIT THE FROG APPEARS*")

    qwery = input("FIGHT OR BEG FOR MERCY? F/M ").upper()

    if qwery == "F":
        print("YOU DEAL DAMAGE TO HIM... 1 DAMAGE???")
        print("kermit the frog deals 1 damage to you")
        player_hp -= 1
        print(f"you have {player_hp} HP left!")

    elif qwery == "M":
        print("You begged and pleaded for mercy")
        print('KERMIT THE FROG says "i was sparing you bucko"')

        q = input("NOW WHAT? F/C/R ? ").upper()
        if q == "F":
            print("you hit kermit for one damage again. HOW?!?!?")
            print("kermit is no longer sparing you")
            player_hp -= 9999999999
            print(f"you died with {player_hp}")

input("\nPress ENTER to exit game")


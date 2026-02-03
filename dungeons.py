import random

gold = 0
player_hp = 30

print("HELLO DUNGEON CRAWLER!")

answer = input("ARE YOU READY TO GO IN THE DUNGEON??? Y/N ").upper()

if answer == "N":
    input("ok bye, hit enter to leave")
    exit()

print("*hear that?*")
print("*eyes glow in the dark*")

# ---------- FIRST ENEMY ----------
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
    exit()

# ---------- FIRST BATTLE LOOP ----------
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
            exit()

# ---------- NEXT ACTION ----------
print("\nYou move deeper into the dungeon...")
action = input("What to do now? S(hop), W(all), E(xplore): ").upper()

if action == "W":
    print("You find strange writings on the wall...")
    input("All you can read is: '✈︎🕈︎☜︎☼︎❄︎☪︎ 💧︎❄︎🕆︎👎︎✋︎⚐︎ ☝︎✌︎💣︎☜︎💧︎'")

elif action == "E":
    print("\n*The ground shakes...*")

    # ---------- STRONG MONSTER RNG ----------
    strong_monsters = ["Orc", "Troll", "Rock Monster", "Giant Spider"]
    strong = random.choice(strong_monsters)

    strong_hp = random.randint(20, 35)
    strong_min_dmg = 6
    strong_max_dmg = 12

    print(f"A {strong} appears!")

    if input("FIGHT, CHECK, OR RUN? F/C/R ").upper() == "R":
        print("You barely escape...")
        exit()

    # ---------- SECOND BATTLE LOOP ----------
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

        strong_damage = random.randint(strong_min_dmg, strong_max_dmg)
        player_hp -= strong_damage
        print(f"The {strong} smashes you for {strong_damage} damage!")
        print(f"Your HP: {player_hp}")

        if player_hp <= 0:
            print("The dungeon claims another victim...")
            exit()

print(f"\nYou survive with {player_hp} HP and {gold} GOLD!")
elif qwery == "S":
    print("Welcome to the Shop!")
    buy1 = input("Would you like to buy a H(ealing Item), or a B(etter Sword?)")
    if buy1 == "H":
        gold -= 5
        print("You bought a Healing Item for 5 GOLD")
    elif buy1 == 
input("\nPress ENTER to exit game")


    
  # ✈︎🕈︎☜︎☼︎❄︎☪︎ 💧︎❄︎🕆︎👎︎✋︎⚐︎ ☝︎✌︎💣︎☜︎💧︎

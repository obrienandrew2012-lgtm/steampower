import random

print("HELLO DUNGEON CRAWLER!")

player_hp = 30  # your health

answer = input("ARE YOU READY TO GO IN THE DUNGEON??? Y/N ")

if answer == "N":
    input("ok bye, hit enter to leave")
    exit()

elif answer == "Y":
    quest1 = input("GREAT! you're there now GOOD LUCK!! ")
    print(quest1)

print("*hear that?*")
print("*eyes glow in the dark*")

# --- Creature list ---
creatures = ["Goblin", "Slime", "Skeleton", "Bat", "Tiny Demon"]
creature = random.choice(creatures)

print(f"A {creature} appears!")

beast1 = input("FIGHT, CHECK THEIR STATS, OR RUN? F/C/S ")

if beast1 == "C":
    print(f"{creature} HP: 10")
    print("Damage per hit: 5")
    beast1 = input("Now what? FIGHT OR RUN? F/S ")

if beast1 == "S":
    print("You run away safely...")
    input("Press ENTER to exit")
    exit()

if beast1 == "F":
    # --- Player attack ---
    player_damage = random.randint(8, 20)
    print(f"You attack the {creature}!")
    print(f"You deal {player_damage} damage!")

    # --- Creature attack ---
    creature_damage = random.randint(3, 8)
    player_hp -= creature_damage

    print(f"The {creature} hits you back for {creature_damage} damage!")
    print(f"Your HP is now {player_hp}")

    if player_hp <= 0:
        print("You died in the dungeon...")
    else:
        print("You survived the encounter!")

input("\nPress ENTER to exit game")

    
  # ✈︎🕈︎☜︎☼︎❄︎☪︎ 💧︎❄︎🕆︎👎︎✋︎⚐︎ ☝︎✌︎💣︎☜︎💧︎

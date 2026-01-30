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

# --- Creature stats ---
creature_hp = 10

if beast1 == "C":
    print(f"{creature} HP: {creature_hp}")
    print("Damage per hit: 3–8")
    beast1 = input("Now what? FIGHT OR RUN? F/S ")

if beast1 == "S":
    print("You run away safely...")
    input("Press ENTER to exit")
    exit()

# --- REAL FIGHT LOOP ---
if beast1 == "F":
    print(f"You engage the {creature} in battle!")

    while player_hp > 0 and creature_hp > 0:

        # Player attack
        player_damage = random.randint(8, 20)
        creature_hp -= player_damage
        print(f"\nYou strike the {creature} for {player_damage} damage!")

        if creature_hp <= 0:
            print(f"The {creature} collapses! You win!")
            break

        # Creature attack
        creature_damage = random.randint(3, 8)
        player_hp -= creature_damage
        print(f"The {creature} hits you for {creature_damage} damage!")
        print(f"Your HP: {player_hp} | {creature} HP: {creature_hp}")

        if player_hp <= 0:
            print("You fall to the dungeon floor... You died.")
            break
if input("What do you do now?") == "wall" or "WALL" or "Wall" or "W":
    print("you find writings on the wall")
    print("it appears to be in some sort of language...")
    input("all you could make out was the developer's name... '✈︎🕈︎☜︎☼︎❄︎☪︎ 💧︎❄︎🕆︎👎︎✋︎⚐︎ ☝︎✌︎💣︎☜︎💧︎' it appears to be in a language called 'wingdings'")
input("\nPress ENTER to exit game")


    
  # ✈︎🕈︎☜︎☼︎❄︎☪︎ 💧︎❄︎🕆︎👎︎✋︎⚐︎ ☝︎✌︎💣︎☜︎💧︎

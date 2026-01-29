import random
print("HELLO DUNGEON CRAWLER!")

answer = input("ARE YOU READY TO GO IN THE DUNGEON??? Y/N ")

if answer == "N":
    input("ok bye, hit enter to leave")
# the code :)

elif answer == "Y":
    quest1 = input("GREAT! you're there now GOOD LUCK!! ")
    print(quest1)
smallcreatures = print("Small Creatures")
print("*hear that?*")
print("*eyes glow in the dark*")
beast1 = input("SMALL CREATURES APPEAR! FIGHT, CHECK THEIR STATS, OR RUN? F/C/S ")
beast2 = print(f"{smallcreatures} deal 5 Damage to you!")
    print(f"You have {health} HP left!")
health = (int(100))
if beast1 == "F":
    number = random.randint(1, 5)

    if number == 5:
        print("CRITICAL HIT!")
        print("20 DAMAGE")
    else:
        print("You attack!")
        print("12 DAMAGE")
        print("Creatures have 8 HP left!")
        print(beast1)
elif beast1 == "C":
    print("Small Creatures: 20 HP, 5 Damage Per Hit 'Simple Enemies'")
    print(beast1)
else: print("You Ran! Earned Nothing")

input("press enter to exit dungeon")
    
  # ✈︎🕈︎☜︎☼︎❄︎☪︎ 💧︎❄︎🕆︎👎︎✋︎⚐︎ ☝︎✌︎💣︎☜︎💧︎

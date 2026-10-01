#Name:Misa
#Class: 6th Hour
#Assignment: Scenario 1

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead has asked you
#to create a nested dictionary containing five enemy creatures (and their properties)
#for combat testing. Additionally, the testers are asking for a way to input changes
#to the enemy's damage values for balancing, as well as having it print those changes
#to confirm they went through.

#Other than damage which is required, it is up to you to decide what properties are
#important and the theme of the game.

Bosses = {
    "Enemy1" : {
        "Special_Grade" : "4",
        "Skill" : "Sword",
        "Human" : True,
        "Damage" : 50
    },
    "Enemy2" : {
        "Special_Grade" : "8",
        "Skill" : "Psychokinesis",
        "Human" : False ,
        "Damage" : 100
    },
    "Enemy3" : {
        "Special_Grade" : "9",
        "Skill" : "Hydrokinesis",
        "Human" : False,
        "Damage" : 100
    },
    "Enemy4": {
        "Special_Grade": "2",
        "Skill": "Bare Fists",
        "Human": True,
        "Damage" : 50
    },
    "Enemy5": {
        "Special_Grade": "6",
        "Skill": "Sythe",
        "Human": True,
        "Damage" : 50
    },
}
print(Bosses)

Bosses["Enemy1"].update({"Damage" : int(input("Damage for Human Boss 1 1-50: "))})

print("Human Boss 1 Damage Altered")

Bosses["Enemy2"].update({"Damage" : int(input("Damage for Nonhuman Boss 1 1-100: "))})

print("Nonhuman Boss 1 Damage Altered")

Bosses["Enemy3"].update({"Damage" : int(input("Damage for Nonhuman Boss 2 1-100: "))})

print("Nonhuman Boss 2 Damage Altered")

Bosses["Enemy4"].update({"Damage" : int(input("Damage for Human Boss 1 1-50: "))})

print("Human Boss 2 Damage Altered")

Bosses["Enemy5"].update({"Damage" : int(input("Damage for Human Boss 1 1-50: "))})

print("Human Boss 3 Damage Altered")

print(Bosses)

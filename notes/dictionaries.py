# Ib 2nd Dictonaries notes
avatar = {
    "earth":{
        "toph": "My name is toph, cuz it sounds like Tough and thats just what I am."
    },
    "water":{
        "katara": "It's not like I am a preachy crybaby who can't help but make speaches about hope all the time",
        "sokka":"I used to be  bommerang guy."
    },
    "fire": {
        "zuko": "It just keep blowqing up in my face. Like everythimg always does!",
        "Uncle Iroh": "It's nothing but boiled leaf juice"
    },
    "air":{

    "aang":"Will you go penguin sledding with me!?!"
    }
}
print(avatar["earth"]["toph"])
print(avatar["water"]["sokka"])

person = {
    #key: value,
    "name": "Katie",
    "age": 37,
    "job": "coordinator",
    "siblings": ["alex", "Andrew", "vienna", "tia", "Tresyon", "xavier","jake"]
}

print(person["name"])
print(person.keys())
for key in person.keys():
    if key == "siblings":
        for sib in person[key]:
            print(f"{person['name']} has a sivling names {sib}")
    else:
        print(f"{key} is {person[key]}")
print(person.values())
person["age"] += 1
print(person["age"])
person["birthday"] = "June 8"
print(person.items())
person["birthday"] = "october 27"
print(person.items())
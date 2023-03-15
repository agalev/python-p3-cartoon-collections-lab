def roll_call_dwarves(dwarf_list):
    count = 1
    for dwarf in dwarf_list:
        print(f"{count}. {dwarf}")
        count+=1

def summon_captain_planet(planeteer_list):
    output_list = list()
    for planeteer in planeteer_list:
        output_list.append(f"{planeteer.capitalize()}!")
    return output_list
    

def long_planeteer_calls(words_list):
    for word in words_list:
        if len(word) > 4:
            return True
    return False

def find_the_cheese(strings_list):
    cheeses = ['cheddar', 'gouda', 'camembert']
    for ingredient in strings_list:
        for cheese in cheeses:
            if ingredient == cheese:
                return ingredient
    return None

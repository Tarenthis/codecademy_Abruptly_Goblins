# add_gamer adds a new gamer to the gamers dictionary. 
# Each gamer should be represented by a dict <name>:<availbility>
def add_gamer(gamer, gamers_list):
    if gamer.get("name") and gamer.get("availability"):
        gamers_list.append(gamer)
    else:
        print("Gamer missing critical details")

# build_daily_frequency_table takes no argument returns a dictionary with the days of the week as keys and `0`s for values.
def build_daily_frequency_table():
    return {"Monday":0, 
            "Tuesday":0, 
            "Wednesday":0, 
            "Thursday":0, 
            "Friday":0, 
            "Saturday":0, 
            "Sunday":0
            }

# Counts the number of people every night
# The function should iterate through each gamer in `gamers_list` 
# and iterate through each day in the gamer's availability. 
# For each day in the gamer's availability, add one to that date 
# on the frequency table.
def calculate_availability(gamers_list, available_frequency):
    for gamer in gamers_list:
        for availability in gamer.get("availability"):
            available_frequency[availability] += 1
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


def find_best_night(availability_table):
    """
    takes a dictionary `availability_table` and returns the key with the highest number.
    Args:
        availability_table: table populated with total availabilities for each day of all gamers in gamers list

    Returns:
        the day of the week with the highest availabilities 
    """
    # Method 1
    values = list(availability_table.values())
    keys = list(availability_table.keys())
    return keys[values.index(max(values))]

    # Method 2
    # best_availability = 0
    # best_day = "NULL"
    # for day, availability in availability_table.items():
    #     if availability > best_availability:
    #         best_availability = availability
    #         best_day = day
    # return best_day

def available_on_night(gamers_list, day):
    """
    takes two parameters: `gamers_list` and `day` and returns a list of people who are available on that particular day.
    Args:
        gamers_list: list containing dictionary elements representing each gamer
        day: string representing the day of the week most gamers are available determined by find_best_night()
    Returns:
        A list containing the dictionary for each gamer that is available on 'day'
    """
    available_gamers = []
    for gamer in gamers_list:
        if day in gamer.get("availability"):
            available_gamers.append(gamer)
    return available_gamers

# Define email format
form_email = """
Greetings {name}! The Secret Sorcerey Society has decided that we shall convene on {day_of_week} to engage in a battle of {game}. 

We hope you will be able to join us and await your arrival. 

Magically Yours,
The Secret Sorcerey Society
"""

def send_email(gamers_who_can_attend, day, game):
    """
    Print `form_email` for each gamer in `gamers_who_can_attend` with their 'name' and appropriate `day` and `game`.
    Args:
        gamers_who_can_attend: List of gamer dictionaries who can attend on 'day'
        day: The best night for gamer availabilities 
        game: Name of the game being played
    Output:
        Email for each gamer attending that day 
    """
    for gamer in gamers_who_can_attend:
        print(form_email.format(name=gamer["name"], day_of_week=day, game=game))
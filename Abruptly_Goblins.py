from ag_functions import *

# Initialize list of empty list that will contain gamers attending game night 
gamers = []

# Add gamers using add_gamer function
kimberly = {"name":"Kimberly Warner", "availability":["Monday", "Tuesday", "Friday"]}
add_gamer(kimberly, gamers)
add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)

# Initialize count_availability dictionary with build_daily_frequency_table()
count_availability = build_daily_frequency_table()

# Calculate gamer availability based off gamers and populate count_availability with availabilities 
calculate_availability(gamers, count_availability)

# Find the best night for gamer availability 
game_night = find_best_night(count_availability)

# Find the gamers that are available on game_night 
attending_game_night = available_on_night(gamers, game_night)



print(count_availability)
print(game_night)
print(attending_game_night)
print("\n\n Emails:")
send_email(attending_game_night, game_night, "Abruptly Goblins!")
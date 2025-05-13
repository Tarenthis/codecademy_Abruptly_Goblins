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

# Send emails to those who can attend game_night
print("First game night emails:")
send_email(attending_game_night, game_night, "Abruptly Goblins!")

# Afterward: 
# List of gamers who cannot attend game_night
unable_to_attend_best_night = [gamer for gamer in gamers if game_night not in gamer['availability']]

# Build a second frequency table for second_night
second_night_availability = build_daily_frequency_table()

# Calculate availability of gamers who could not attend game_night
calculate_availability(unable_to_attend_best_night, second_night_availability)

# Find the second best game night
second_night = find_best_night(second_night_availability)

# Create list of those available on second_night (including those who attended first)
available_second_game_night = available_on_night(gamers, second_night)

# Send an email to everyone who can attend the second night 
print("————————————————————————————————————————————————————————————————————")
print("Second game night emails:")
send_email(available_second_game_night, second_night, "Abruptly Goblins!")

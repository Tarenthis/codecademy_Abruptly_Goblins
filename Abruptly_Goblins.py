from ag_functions import *

# Initialize list of empty list that will contain gamers attending game night 
gamers = []

# Define and add first gamer using add_gamer function
kimberly = {"name":"Kimberly Warner", "availability":["Monday", "Tuesday", "Friday"]}
add_gamer(kimberly, gamers)

# Add additional gamers
add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)

# Initialize coun_availability dictionary with build_daily_frequency_table()
count_availability = build_daily_frequency_table()
calculate_availability(gamers, count_availability)

print(find_best_night(count_availability))

print(count_availability)


"""
3
1 5
10 3
3 4
"""


fuel_amounts = [1, 10, 3]
distances    = [5, 3, 4] # distance to the next station


starting_station = 0
current_fuel = 0

for station_number, fuel_amount in enumerate(fuel_amounts):
    current_fuel += fuel_amount # fill in at the pump
    current_fuel -= distances[station_number] # let's travel to the next station!
    if current_fuel < 0:
        # we did not get to the next station, we are absolutely fucked
        # Suppose our starting station was S1
        # we managed to drive S1 -> S2 -> S3 but we did not get to S4
        # this means we need to start again, but suprisingly not at S2. 
        # We can go straight to S4. (Why is that though?)
        starting_station = station_number + 1
        current_fuel = 0

# because tasks says there is a guaranteed answer, 
# let's return whatever we found
print(starting_station)
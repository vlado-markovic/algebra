import random

# 7 is neutral, from 0 to 14
def ph_values():
    return [random.randint(0 , 14)]

# in lux    
def plant_light():
    return [random.randint(150 , 300)]

# in percentages, averages   
def soil_humidity():
    return [random.randint(10 , 45)]
    
# Salt concentration of the soil water 
# (saturation extract)	Salinity
# 0 - 3	                0 - 4.5	        non saline
# 3 - 6              	4.5 - 9	        slightly saline
# 6 - 12            	9 - 18	        medium saline
# more than 12	        more than 18	highly saline    
def soil_salinity():
    return [random.randint(0 , 18)]

# The average soil temperatures for bioactivity range from 50 to 75°F (10-24°C).
def soil_temperature():
    return [random.randint(10 , 24)]

# Celsius degrees 
def room_temperature():
    return [random.randint(0 , 30)]
        
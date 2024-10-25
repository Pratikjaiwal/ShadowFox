def format_string(num, char):
    formatted_string = "{}{}".format(num, char)
    return formatted_string
result_1 = format_string(145, 'o')
print("Formatted String:", result_1)
import math
def pond_area_and_water(r, water_per_square_meter):
    pi = 3.14
    pond_area = pi * (r ** 2)
    total_water = int(pond_area * water_per_square_meter)
    return pond_area, total_water
radius = eval(input())  # in meters
water_per_sq_meter = eval(input())  
pond_area, total_water = pond_area_and_water(radius, water_per_sq_meter)
print("Pond Area:", pond_area, "square meters")
print("Total Water in the pond:", total_water, "liters")
def calculate_speed(distance, time):
    speed = int(distance / time)
    return speed
distance = eval(input())  
time_minutes = eval(input())  
time_seconds = time_minutes * 60  
speed = calculate_speed(distance, time_seconds)
print("Speed:", speed, "meters per second")

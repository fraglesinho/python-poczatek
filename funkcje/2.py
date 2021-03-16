def avg_speed(distance, time):
    return distance / time

# run_distance = float(input("Ile km przebiegłeś? "))
# run_time = float(input("Ile godzin Ci to zajeło? "))
# bike_distance = float(input("Ile km przejechałes rowerem? "))
# bike_time = float(input("Ile godzin Ci to zajeło? "))
# car_distance = float(input("Ile km przejechałeś autem? "))
# car_time = float(input("Ile godzin Ci to zajeło? "))

def run_avg_speed_calculator(vehicle_name):
    distance = float(input(f"Ile km pokonałeś za pomocą {vehicle_name}? "))
    time = float(input("Ile godzin Ci to zajeło? "))
    average_speed = avg_speed(distance, time)
    print(f"Twoja średnia prędkość przemiszczania się {vehicle_name} to {average_speed}km/h")

run_avg_speed_calculator("biegu")
run_avg_speed_calculator("roweru")
run_avg_speed_calculator("samochodu")
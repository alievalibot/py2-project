import time
from functions import convert_length, convert_weight, convert_temp, convert_cm_m, convert_currency


sleep_time = 5

length_objects = ["km", "miles"]
weight_objects = ["kg", "pounds"]
valute_objects = ["USD", "EUR"]
cm_m_objects = ["cm", "m"]
temp_units = ["C", "F"]


length_coeffs = [0.621371, 1 / 0.621371]
cm_m_coeffs = [0.01, 100]
weight_coeffs = [2.20462, 1 / 2.20462]
temp_coeffs = [[9/5, 32], [5/9, -32 * 5/9]]

choice = None
while choice != "0":
    print("\n=== ^_^ Unit Converter ^_^ ===")
    print("1 - Kilometers -> Miles")
    print("2 - Miles -> Kilometers")
    print("3 - Centimeters -> Meters")
    print("4 - Meters -> Centimeters")
    print("5 - Celsius -> Fahrenheit")
    print("6 - Fahrenheit -> Celsius")
    print("7 - Kilograms -> Pounds")
    print("8 - Pounds -> Kilograms")
    print("9 - USD -> EUR ")
    print("10 - EUR -> USD ")
    print("0 - Exit")

    choice = input("Your choice: ")
    
    if choice == "0":
        print("Exiting program.")
        break
    
    elif choice == "1":
        v = float(input("Enter kilometers: "))
        print("Thinking...")
        time.sleep(sleep_time)
        print(f"{v} km = {convert_length(1, v)} miles")
        
    elif choice == "2":
        v = float(input("Enter miles: "))
        print("Thinking...")
        time.sleep(sleep_time)
        print(f"{v} miles = {convert_length(2, v)} km")
        
    elif choice == "3":
        v = float(input("Enter centimeters: "))
        print("Thinking...")
        time.sleep(sleep_time)
        print(f"{v} cm = {convert_cm_m(1, v)} m")
        
    elif choice == "4":
        v = float(input("Enter meters: "))
        print("Thinking...")
        time.sleep(sleep_time)
        print(f"{v} m = {convert_cm_m(2, v)} cm")
        
    elif choice == "5":
        v = float(input("Enter °C: "))
        print("Thinking...")
        time.sleep(sleep_time)
        print(f"{v} °C = {convert_temp(1, v)} °F")
        
    elif choice == "6":
        v = float(input("Enter °F: "))
        print("Thinking...")
        time.sleep(sleep_time)
        print(f"{v} °F = {convert_temp(2, v)} °C")
        
    elif choice == "7":
        v = float(input("Enter kilograms: "))
        print("Thinking...")
        time.sleep(sleep_time)
        print(f"{v} kg = {convert_weight(1, v)} pounds")
        
    elif choice == "8":
        v = float(input("Enter pounds: "))
        print("Thinking...")
        time.sleep(sleep_time)
        print(f"{v} pounds = {convert_weight(2, v)} kg")
        
    elif choice == "9":
        v = float(input("Enter USD: "))
        print("Thinking...")
        time.sleep(sleep_time)
        print(f"{v} USD = {convert_currency(1, v)} EUR")
        
    elif choice == "10":
        v = float(input("Enter EUR: "))
        time.sleep(sleep_time)
        print("Thinking...")
        print(f"{v} EUR = {convert_currency(2, v)} USD")

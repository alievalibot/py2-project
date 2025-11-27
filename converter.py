import time
from functions import convert_length, convert_weight, convert_temp, convert_cm_m, convert_currency
import time

sleep_time = 5

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

    try:
        if choice in ["1","2","3","4","5","6","7","8","9","10"]:
            v = float(input("Enter amount: "))
        else:
            print("Invalid option!")
            continue

    except ValueError:
        print("Error: please enter a number!")
        continue
    
    print("Thinking...")
    time.sleep(sleep_time)

    if choice == "1":
        print(f"{v} km = {convert_length(1, v)} miles")

    elif choice == "2":
        print(f"{v} miles = {convert_length(2, v)} km")

    elif choice == "3":
        print(f"{v} cm = {convert_cm_m(1, v)} m")

    elif choice == "4":
        print(f"{v} m = {convert_cm_m(2, v)} cm")

    elif choice == "5":
        print(f"{v} °C = {convert_temp(1, v)} °F")

    elif choice == "6":
        print(f"{v} °F = {convert_temp(2, v)} °C")

    elif choice == "7":
        print(f"{v} kg = {convert_weight(1, v)} pounds")

    elif choice == "8":
        print(f"{v} pounds = {convert_weight(2, v)} kg")

    elif choice == "9":
        print(f"{v} USD = {convert_currency(1, v)} EUR")

    elif choice == "10":
        print(f"{v} EUR = {convert_currency(2, v)} USD")


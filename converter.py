import forex_python.converter
import time

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


value_coeffs = [None, None]  
c_rates = forex_python.converter.CurrencyRates()

def convert_length(option, value):
    if option == 1:
        return value * length_coeffs[0]
    else:
        return value * length_coeffs[1]

def convert_weight(option, value):
    if option == 1:
        return value * weight_coeffs[0]
    else:
        return value * weight_coeffs[1]

def convert_temp(option, value):
    a = temp_coeffs[option - 1][0]
    b = temp_coeffs[option - 1][1]
    return value * a + b

def convert_cm_m(option, value):
    if option == 1:
        return value * cm_m_coeffs[0]
    else:
        return value * cm_m_coeffs[1]

def convert_currency(option, value):
    if value_coeffs[0] is None:
        rate = c_rates.get_rate('USD', 'EUR')
        value_coeffs[0] = rate         
        value_coeffs[1] = 1.0 / rate   
    if option == 1:
        return value * value_coeffs[0]
    else:
        return value * value_coeffs[1]

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

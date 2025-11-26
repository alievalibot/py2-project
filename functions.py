import forex_python.converter
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
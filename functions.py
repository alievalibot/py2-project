length_objects = ["km", "miles"]
weight_objects = ["kg", "pounds"]
valute_objects = ["USD", "EUR"]
cm_m_objects = ["cm", "m"]
temp_units = ["C", "F"]


length_coeffs = [0.621371, 1 / 0.621371]
cm_m_coeffs = [0.01, 100]
weight_coeffs = [2.20462, 1 / 2.20462]
temp_coeffs = [[9/5, 32], [5/9, -32 * 5/9]]

def convert_length(option, value):
    if option == 1:
        return value * length_coeffs[0]
    else:
        return value * length_coeffs[1]
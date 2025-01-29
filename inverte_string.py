def inverter_string():
    entrada = input("Informe uma string: ")
    string_invertida = ""
    for char in entrada:
        string_invertida = char + string_invertida
    print(string_invertida)

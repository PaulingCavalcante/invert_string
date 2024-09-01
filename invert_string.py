def invert_string(str):
    invert = ""
    for letter in str:
        invert = letter + invert
    return invert

string = input("Digite uma String para inverter: ")
string_invert = invert_string(string)

print(f"String original: {string}")
print(f"String invertida: {string_invert}")
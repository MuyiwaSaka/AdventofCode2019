import math

def round_down(numb, decimals=0):
    multiplier = numb ** decimals;
    return math.floor(numb*multiplier)/multiplier

def get_fuel_module(modcnt):
    return round_down(modcnt/3)-2

def find_last_fuel_value(fval):
    fr=fval
    ft = 0
    while fr > 0 :
        fr = get_fuel_module(fr)
        if fr > 0:
            ft = ft + fr
    return ft

# Calculate the values and print the output
santa_fuel=0
santa_neg_fuel = 0
f = open("day1 input.txt")
for r in f:
    santa_fuel = santa_fuel + get_fuel_module(int(r))
    santa_neg_fuel = santa_neg_fuel + find_last_fuel_value(int(r))
print("Santa's fuel is {}".format(int(santa_fuel)))
print("Santa's Recursive Fuel is {}".format(int(santa_neg_fuel)))
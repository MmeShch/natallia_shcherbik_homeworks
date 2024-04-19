# 3) Написать 12 функций по переводу: 1. Дюймы в сантиметры,2. Сантиметры в дюймы,3. Мили в километры
# 4. Километры в мили, 5. Фунты в килограммы, 6. Килограммы в фунты, 7. Унции в граммы, 8. Граммы в унции
# 9. Галлон в литры, 10. Литры в галлоны, 11. Пинты в литры, 12. Литры в пинты

#1)
# def convert_inch_to_cm(inch):
#     cm = 2.54 * inch
#     return round(cm, 2)
#
#
# inp_inch = float(input("Enter inches: "))
# centimeter = convert_inch_to_cm(inp_inch)
# print(f'{inp_inch} is equal to {centimeter} centimeters')

# 2)
# def convert_cm_to_inch(cm):
#     inch = cm / 2.54
#     return round(inch, 2)
#
#
# inp_cm = float(input("Enter centimeters: "))
# inches = convert_cm_to_inch(inp_cm)
# print(f'{inp_cm} centimeters is equal to {inches} inches')

# 3)
# def convert_mile_to_km(mile):
#     km = 1.60934 * mile
#     return round(km, 2)
#
#
# inp_mile = float(input('Enter miles: '))
# kilometers = convert_mile_to_km(inp_mile)
# print(f'{inp_mile} mile(s) is equal to {kilometers} km')

# 4)
# def convert_km_to_mile(km):
#     mile = 0.6213 * km
#     return round(mile, 2)
#
#
# inp_km = float(input('Enter kilometers: '))
# miles = convert_km_to_mile(inp_km)
# print(f'{inp_km} kilometers is equal to {miles} miles')

#5)

# def pound_to_klg(pound):
#     klg = 0.4536 * pound
#     return round(klg, 2)
#
#
# inp_pound = float(input('Enter pounds: '))
# kilograms = pound_to_klg(inp_pound)
# print(f'{inp_pound} pounds is equal to {kilograms} kilos')

# 6)
# def klg_to_pound(klg):
#     pound = 2.2046 * klg
#     return round(pound, 2)
#
#
# inp_klg = float(input('Enter kilograms : '))
# pounds = klg_to_pound(inp_klg)
# print(f'{inp_klg} kilograms is equal to {pounds} pounds')

# 7)
# def ounce_to_gram(ounce):
#     gram = 28.3495 * ounce
#     return round(gram, 2)
#
#
# inp_ounce = float(input('Enter ounces : '))
# grams = ounce_to_gram(inp_ounce)
# print(f'{inp_ounce} ounces is equal to {grams} grams')

# 8)
# def gram_to_ounce(gram):
#     ounce = 0.3527 * gram
#     return round(ounce, 2)
#
#
# inp_gram = float(input('Enter grams : '))
# ounces = gram_to_ounce(inp_gram)
# print(f'{inp_gram} grams is equal to {ounces} ounces')

# 9)
# def gallon_to_liter(gallon):
#     liter = 3.78541 * gallon
#     return round(liter, 2)
#
#
# inp_gallon = float(input('Enter gallons : '))
# liters = gallon_to_liter(inp_gallon)
# print(f'{inp_gallon} gallons is equal to {liters} liters')

# 10)

# def liter_to_gallon(liter):
#     gallon = 0.2642 * liter
#     return round(gallon, 2)
#
#
# inp_liter = float(input('Enter liters : '))
# gallons = liter_to_gallon(inp_liter)
# print(f'{inp_liter} liters is equal to {gallons} gallons')

# 11)

# def pint_to_liter(pint):
#     liter = 0.568261 * pint
#     return round(liter, 2)
#
#
# inp_pint = float(input('Enter pints : '))
# liters = pint_to_liter(inp_pint)
# print(f'{inp_pint} pints is equal to {liters} liters')

# 12)

# def liter_to_pint(liter):
#     pint = 2.1133 * liter
#     return round(pint, 2)
#
#
# inp_liter = float(input('Enter liters : '))
# pints = liter_to_pint(inp_liter)
# print(f'{inp_liter} liters is equal to {pints} pints')

# Program   askes user for a temperature and then shows the windchill value for that wing spee and temp. 
# At temp 8.0f and wind speed of 5 mph  windchill is : -1.11f 
# 5-60 
# At temp x and wind speed of y+5 mph  windchill is : x 
# Celsius to Fahrenheit      is Celsius  times 9/5  plus 32
# Float w /2 decimals
 

temp = float(input("what is the Temp? "))
corf = str(input("is that Fahrenheit or Celsius? (F/C) ")).lower()

wind_speed = 5

if corf == "c":
    temp = (9/5) * temp + 32

if corf == "c" or corf == "f":
    while wind_speed <= 60:
        wind_chill = 35.74 + 0.6215 * temp - 35.75 * (wind_speed ** 0.16) + 0.4275 * temp * (wind_speed ** 0.16)
        print(f"At temp {temp}F and wind speed of {wind_speed} mph. The windchill is : {wind_chill:.2f}")
        wind_speed = wind_speed + 5

else:
    print(f"Go get a coat on!")
def kelvintoFahrenheit(temperature):
    assert (temperature >=0)," Colder than absolute zero at MTCA!"
    res=((temperature--273)*1.8)+32
    return res
try:
    print (kelvintoFahrenheit(-50))
except Exception as ob:
    print(ob)
try:
    print (kelvintoFahrenheit(273))
except Exception as ob:
    print(ob)
try:
    print (kelvintoFahrenheit(505.78))
except Exception as ob:
    print(ob)
try:
    print (kelvintoFahrenheit(-5))
except Exception as ob:
    print(ob)
print("thank you")

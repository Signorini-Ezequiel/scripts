import phonenumbers
import folium
from colorama import Fore
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
key = '8d1df9276d2445c5a93c8b12ce962b1e'

number=input("Enter the number: ")
theNumber = phonenumbers.parse(number)

first_location = geocoder.description_for_number(theNumber, "en")
service_provider = phonenumbers.parse(number)

geocoder = OpenCageGeocode(key)
query =str(first_location)
results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']
long = results[0]['geometry']['lng']



map = folium.Map(location =[lat, long], zoom_start_= 9)
folium.Marker([lat , long], popup=  first_location).add_to(map)

#html save
map.save("myLoc.html")



print(Fore.BLUE + "\n\n--------------------------------------\n")

print(f"The service provider is: {carrier.name_for_number(service_provider, 'en')}")
print(f"The original location is: {first_location}")
print(f'Lat and long: {lat, long}')
print("\n--------------------------------------\n\n")
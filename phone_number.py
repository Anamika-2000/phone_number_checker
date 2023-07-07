
import phonenumbers
import opencage
import folium

from phonenumbers import timezone,geocoder,carrier
from opencage.geocoder import OpenCageGeocode

phone=input('phone number')
x = phonenumbers.parse(phone, "CH")#entering phone number
print("Your phone number is: ")
print(x)

timezone=timezone.time_zones_for_number(x)#time zone
print("time zone is: ")
print(timezone)

carrier=carrier.name_for_number(x,'en')#carrier like airtel

location=geocoder.description_for_number(x,'en') #to show region like india

print("Your company is :",carrier)

print("Your region is :",location)


key='3675876a7af74111b1852b9de8953467'
geocoder=OpenCageGeocode(key)
query=str(location)
result=geocoder.geocode(query)
print("The full latitude and longitude location are:")
print(result)

lat=result[0]['geometry']['lat']
lng=result[0]['geometry']['lng']
print("The latitude and longitude location are:")
print(lat,lng)

myMap=folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=location).add_to(myMap)

myMap.save("myloc.html")

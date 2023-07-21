import phonenumbers
from phonenumbers import geocoder, carrier
import folium
from geopy.geocoders import Nominatim
import tkinter as tk
from tkinter import messagebox

def lookup_phone():
    phone = phone_entry.get()

    try:
        # Parse the phone number
        x = phonenumbers.parse(phone, "CH")
        parsed_number.set("Your phone number with country code is: " + str(x))

        # Get the carrier information
        carrier_name = carrier.name_for_number(x, 'en')
        carrier_info.set("The company from which the SIM was bought is: " + carrier_name)

        # Get the location information
        location = geocoder.description_for_number(x, 'en')
        location_info.set("Your location is: " + location)

        # Geocode the location
        geolocator = Nominatim(user_agent="my_app")
        query = location + ", " + location
        geocode = geolocator.geocode(query)

        if geocode is not None:
            lat = geocode.latitude
            lng = geocode.longitude
            map_info.set("The latitude and longitude for " + location + " are: " + str(lat) + ", " + str(lng))

            # Create a map and add a marker
            myMap = folium.Map(location=[lat, lng], zoom_start=9)
            folium.Marker([lat, lng], popup=location).add_to(myMap)

            # Save the map to an HTML file
            myMap.save("myloc.html")
            messagebox.showinfo("Map Saved", "Map saved to myloc.html")
        else:
            map_info.set("Location not found.")

    except phonenumbers.NumberParseException:
        messagebox.showerror("Invalid Phone Number", "Please enter a valid phone number.")

# Create the GUI
root = tk.Tk()
root.title("Phone Number Lookup")
root.geometry("400x300")

# Phone Number Entry
phone_label = tk.Label(root, text="Enter phone number along with country code :")
phone_label.pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

# Button to lookup phone number
lookup_button = tk.Button(root, text="Lookup", command=lookup_phone)
lookup_button.pack()

# Result Labels
parsed_number = tk.StringVar()
carrier_info = tk.StringVar()
location_info = tk.StringVar()
map_info = tk.StringVar()

parsed_label = tk.Label(root, textvariable=parsed_number)
parsed_label.pack()
carrier_label = tk.Label(root, textvariable=carrier_info)
carrier_label.pack()
location_label = tk.Label(root, textvariable=location_info)
location_label.pack()
map_label = tk.Label(root, textvariable=map_info)
map_label.pack()

root.mainloop()
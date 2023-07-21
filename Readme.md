# Phone Number Geolocation Mapping

<p align="center">
This project provide the county code, phone number, the service provider name and the location of the phone number.
This Python script allows you to retrieve the geolocation information for a given phone number and display it on a map using Folium.

<p align="center">
    <a href="Readme.md"><strong>Explore the docs »</strong></a>
<br>
<br>
    <a href="https://github.com/Anamika-2000/phone_number_checker">View Demo</a>
    ·
    <a href="https://github.com/Anamika-2000/phone_number_checker/issues/new">Report Bug</a>
    ·
    <a href="https://github.com/Anamika-2000/phone_number_checker/issues/new">Request Feature</a>

## Table of content
- [Usage](#usage)
- [Description ](#description)
- [Pre-Requisites](#pre-requisites)
- [Authorization](#authorization)
- [Setup](#setup)

<p align="right">
 <a href="#phone-number-geolocation-mapping">Back to top</a>
</p>


## Usage

 The Phone Number Geolocation Mapping can be used to find the basic information related to a phone number.

 
<p align="right">
 <a href="#phone-number-geolocation-mapping">Back to top</a>
</p>

## Description
The Phone Number Geolocation Mapping project is a Python script that allows users to retrieve the geolocation information for a given phone number and display it on a map using the Folium library. By leveraging the phonenumbers and geopy libraries, the script enables users to input a phone number and obtain the associated geolocation details such as the country, region, and carrier information. It then utilizes a geocoding service to convert the location information into latitude and longitude coordinates. The obtained coordinates are used to generate a map using Folium, with a marker indicating the geolocation on the map.

### Functionality
<ul>
<li> Show the county code and the phone number seprately.
<li> Show the name of service provider company from whom SIM card was bought.
<li>Show the country name where the SIM card is present 
<li>Show the latetude and longitude location of the SIM card.
<li>Show the geo location on map. 
</ul>

<p align="right">
 <a href="#phone-number-geolocation-mapping">Back to top</a>
</p>

## Pre-Requisites

- Python 3.x
- phonenumbers library (install using `pip install phonenumbers`)
- geopy library (install using `pip install geopy`)
- tkinter
- folium library (install using `pip install folium`)


<p align="right">
 <a href="#phone-number-geolocation-mapping">Back to top</a>
</p>

## Authorization

There is no specific authorization for this project. 

<p align="right">
 <a href="#phone-number-geolocation-mapping">Back to top</a>
</p>

## Setup
   
### Local Deployment

1. Firstly clone the repository
```
git clone https://github.com/Anamika-2000/phone_number_checker.git
```
2. Import as python project and run the script. 

### Run the application
1. Install the required libraries using the commands mentioned in the "Prerequisites" section.

2. Obtain an API key from OpenCage Geocoder by signing up at [https://opencagedata.com](https://opencagedata.com). Replace `'YOUR_OPENCAGE_API_KEY'` in the code with your actual OpenCage API key.

3. Run the script and follow the prompts:
   - Enter the phone number for which you want to retrieve the geolocation information The phone number should contain the courty code.

Note: The accuracy of geolocation results may vary based on the availability and reliability of data sources.

<p align="right">
 <a href="#phone-number-geolocation-mapping">Back to top</a>
</p>
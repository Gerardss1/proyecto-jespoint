from geopy.geocoders import Nominatim

def get_direccion_gera(lat:str, lon:str):
    geolocator = Nominatim(user_agent= "gerardss")
    location =geolocator.reverse(f"{lat},{lon}")
    return location.address


from helper import input_helper, table_helper
import arg_parser
from geopy.geocoders import Nominatim
import geocoder

def main():
    print(arg_parser.args.debug)
    input_helper.check_argv()
    table_helper.print_computer_hardware_details()

    # geolocator = Nominatim(user_agent="computer_hardware")
    # location = geolocator.geocode("192.168.1.15")
    # print(location.address)
    # print((location.latitude, location.longitude))

    # g = geocoder.ip('me') # gives location of petah tikva
    # print(g.latlng)

    # latitude = ", ".join([str(i) for i in g.latlng])
    # print(latitude)
    # locname = loc.reverse(latitude)
    # print(locname)
    #
    # geolocator = Nominatim(user_agent="my_app")
    # location = geolocator.geocode("israel")
    # print(location)

if __name__ == "__main__":
    main()
#from django.test import TestCase
from ipwhois import IPWhois
# Create your tests here.
from requests import get
import json
import pycountry

# Create your tests here.
ip = get('https://api.ipify.org').text
print('My public IP address is: {}'.format(ip))

obj = IPWhois(ip)
result = obj.lookup_rdap()

#print(json.dumps(result, indent=4))

country = pycountry.countries.get(alpha_2=result["network"]["country"])
print(country.name)
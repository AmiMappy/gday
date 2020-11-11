import requests as req
import os
import sys

pathname = os.path.dirname(sys.argv[0])
fullpath = os.path.abspath(pathname)

response = req.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY").json()

img_file = response["hdurl"][38:]
print(response["title"])
print("-----------------------------------------------------------------------")
print(response["explanation"])
print("\nCourtesy: " + response["copyright"] + " and NASA(NASA Astronomy Picture of The Day)")

os.system("wget " + response["url"] + " -O " + fullpath + "/temp/" + img_file + " > /dev/null 2>&1")
os.system("fim " + fullpath + "/temp/" + img_file + " > /dev/null 2>&1")
# os.system("rm " + fullpath + "/" + img_file) := instead this is handled by gday script

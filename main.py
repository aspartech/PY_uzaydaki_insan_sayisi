import requests
import json

gelen_cevap = requests.get("http://api.open-notify.org/astros.json")

sayi = gelen_cevap.json()["number"]

print(f"sayi={sayi}")

print("isimleri:")

for kişi in gelen_cevap.json()["people"]:
    print(kişi["name"], "-->",kişi["craft"])
import requests
a = requests.get("https://www.rottentomatoes.com/m/lawless_2012")
print(a.status_code)
# L-DOS X UPDATER
import requests
link = "https://ldosx-updater.netlify.app/update.py"
try:
    out=requests.get(url=link,timeout=3)
except requests.ConnectionError as exception:
    print("Connect to the internet!")
    exit()
if out.status_code==404:
    print("The L-DOS X servers must be down, or non-existent Thanks for trying anyways...")
    exit()
if out.status_code==200:
    print("Connected to servers!")
try:
    ldos=open("ldosx.py","w")
except FileNotFoundError:
    print("Please place this file in the directory as L-DOS X!")
    exit()
f = requests.get(link)
ldos.write(f.text)
print("L-DOS X has been updated.")
ldos.close()
exit()

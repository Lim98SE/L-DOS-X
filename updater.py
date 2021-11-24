# L-DOS X UPDATER
import requests
try:
    out=requests.get(url="https://lim95.netlify.app/updater.html",timeout=3)
except requests.ConnectionError as exception:
    print("Connect to the internet!")
    exit()
if out.status_code==404:
    print("The L-DOS X servers have been discontinued.\nThank you for using L-DOS.")
    exit()
if out.status_code==200:
    print("Connected to servers!")
try:
    ldos=open("ldosx.py","w")
except FileNotFoundError:
    print("Please place this file in the directory as L-DOS X!")
    exit()
link = "https://lim95.netlify.app/updater.html"
f = requests.get(link)
f=f.text
code=f[f.find("<code>")+len("<code>"):f.find("</code>")]
print(code)
ldos.write(code)
print("L-DOS X has been updated.")

import requests
url = "https://www.fast2sms.com/dev/bulk"
payload = "sender_id=FSTSMS&message=This is an automated message by Aalap Personal Bot specifically to gurchet. Ye Message agar aapko mila h to aalap ka bot sahi kam kar rha h\
         aapka din mangalmay ho or ho sakta h aap is msg ko pad ke mujhe phone lagaye par mat lagana its just a test&language=english&route=p&numbers=8789436952"
headers = {
'authorization': "iZoPf8kwIrd7xtSeVAujMY2J6qhvzBFpET3DUbg9KlHLnsCRm48byIsJ4NuP60pVRaxAYhfiqSBO3GZg",
'Content-Type': "application/x-www-form-urlencoded",
'Cache-Control': "no-cache",
}
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)
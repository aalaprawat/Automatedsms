import os
from twilio.rest import Client

account_sid = "AC56cbf44423f5a95358805d29d872c6c9"
account_token = "f07949b62534d59e8b905008bc40378a" 

client = Client(account_sid,account_token)
numbers=["+917000090737","+919877470121","+919131352453",
            "+917389379177","+919542690689","+917000593119","+917000626163","+918921365708"]
for i in numbers :
    client.messages.create(
        to=i,
        from_="+12057843701",
        body = "This is an automated message by Aalap Personal Bot\
         Ye Message agar aapko mila h to aalap ka robot sahi kam kar rha h\
         aapka din mangalmay ho or ho sakta h aap is msg ko pad ke mujhe phone lagaye par mat lagana its just a test")
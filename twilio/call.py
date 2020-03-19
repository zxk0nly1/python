from twilio.rest import Client

account = "AC886ee57e81b71c9bcc63e1e2b01480b7"
token = "4f9dc13b4d24fd071b80a7a5689aca61"
client = Client(account, token)

call = client.calls.create(to="+8613169486128",
                           from_="+15308365308",
                           url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")
print(call.sid)
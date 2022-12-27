from twilio.rest import Client
from config import account_sid, auth_token


client = Client(account_sid,auth_token)

call = client.messages.create(
    to="9299330843",
    from_="6187654055",
    body="https://www.youtube.com/watch?v=diU6xQ3zL_Q&ab_channel=yelooo"
)


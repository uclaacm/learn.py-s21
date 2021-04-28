from twilio.rest import Client
import time

accountSID = '' #insert your twilio account SID here
authToken = '' #insert your twilio account authentication token here
twilioCli = Client(accountSID, authToken)
myTwilioNumber = '' #insert your twilio account number
myCellPhone = '' #insert you actual number here

message = twilioCli.messages.create(body='' + exer, from_=myTwilioNumber, to=myCellPhone) #insert your message in body
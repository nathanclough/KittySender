import requests
import shutil
from twilio.rest import Client

AccountSid = "AC579228cf7aacddc113bd69e007e155f7"
AuthToken = "b231d0136d5f45a9bfb4740076858f26"

def getFact():
    return requests.get("https://catfact.ninja/fact").json()['fact']

def getImageLink():
    return requests.get("https://api.thecatapi.com/v1/images/search").json()[0]['url']

def downloadImage():
    imageLink = getImageLink()
    filename = imageLink.split("/")[-1]
    r = requests.get(imageLink,stream = True)
    r.raw.decode_content = True
    with open(filename,'wb') as f:
        shutil.copyfileobj(r.raw, f)  
    print('Image sucessfully Downloaded: ',filename)

def sendMessage():
    client = Client(AccountSid,AuthToken)
    message = client.messages \
            .create(
                    body=getFact(),
                    media_url=getImageLink(),
                    from_='+12019285286',
                    to='+18329484077'
                )
    
print(getFact())


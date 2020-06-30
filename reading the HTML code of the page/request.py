import requests
from requests.exceptions import HTTPError


link = input("pleas input the link:")
# response has some formation known as 'payload'
res=False
#check if the user start wih https or not
if link[0:8]!="https://":
    link="https://{}".format(link)

try:
    response = requests.get(link)
    print("The link is valid")
    res=True
except:
    print("The link is not valid")
    res=False
if res:

    val=input(str("Do you want to print the html page, yes, or no:"))

    if val.lower()=="yes":
        print(response.text)

    elif val.lower()=="no":
        print("thank you, see you later")
    else:
        print("Wrong entery")
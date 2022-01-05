import requests

url = 'https://cloud4213.herokuapp.com/sensors/'
myobj = {'temp': '37', 'ic':'2021', 'dist':'3' }

x = requests.post(url, data = myobj)

#print the response text (the content of the requested file):

print(x.text)

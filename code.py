import requests

response = requests.get('Api Link') 

#####  Enter your API Link in the parenthesis of the 3rd line as a string value  ####

response = response.json()
print(response)

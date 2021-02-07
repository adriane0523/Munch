import requests

client_id="H964eCj_78jA36l34sAyonzJS5HWkqId"
client_secret="ZTpHQkG2M_Lgq8bi4tp4YMkepSy-f5CvI-h_rYTE"
response = requests.get("https://login.uber.com/oauth/v2/token?client_secret="+client_secret+"&client_id="+ client_id +"&grant_type=client_credentials&scope=eats.store")

# Inspect some attributes of the `requests` repository
json_response = response.json()
print(json_response)

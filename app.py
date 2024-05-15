import requests
from icecream import ic

response = requests.get('https://www.ynet.co.il')
print(response.text)

ic ("This is YNET's HTML code")

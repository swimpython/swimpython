import requests as r

url = 'https://zenquotes.io/api'


mode = 'random'

full_url = f"{url}/{mode}"


res = r.get(full_url).json()

#print(res[0])
print(res[0]["a"])
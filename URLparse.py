from urllib.parse import urlparse

url = 'http://olx.ua/obyavlenie/organayzer-dlya-bagazhnika-cargonizer-maxi-IDmRihc.html'

obj = urlparse(url)

print(obj.scheme)
print(obj.netloc)
print(obj.hostname)
print(obj.geturl())
print(obj.port)
print(obj.path)
print(obj.username)
print(obj.password)
#print(obj.params)
#print(obj.query)
#print(obj.fragment)

import requests

# res = requests.get('http://localhost:5000/')

# res = requests.post('http://localhost:5000/mata-pelajaran/')

res = requests.post('http://localhost:5000/mata-pelajaran/90')

print(res.text)

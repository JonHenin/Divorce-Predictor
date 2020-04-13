import json
import requests
import numpy as np

data = {k: np.random.randint(5) for k in range(54)}

r = requests.post('http://35.237.214.19', json=data)

divorce_results = r.json()['divorce']

print(f'Your likelihood of divorce is {divorce_results * 100:.2f}%.')
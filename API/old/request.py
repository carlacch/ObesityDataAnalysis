# CLIENT
import requests
import json

url = 'http://localhost:5000/api/'

# Sous forme : Gender, Age, family_history_with_overweight, FAVC, FCVC, NCP, CAEC, SMOKE, CH2O, SCC, FAF, TUE, CALC, MTRANS
# Gender : 0 ou 1   family_history_with_overweight : 0 ou 1
# FAVC : 0 ou 1     FCVC : 1, 2 ou 3        NCP : 1, 2, 3 ou 4
# CAEC : 0, 1, 2 ou 4       SMOKE : 0 ou 1      CH2O: 1, 2 ou 3
# SCC : 0 ou 1      FAF : 0, 1, 2 ou 3      TUE : 0, 1 ou 2
# CALC : 0, 1, 2 ou 3       MTRANS : 1, 2, 3, 4 ou 5

data = [[0, 22, 0, 1, 3, 3, 1, 0, 2, 0, 1, 2, 1, 4]]
j_data = json.dumps(data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data, headers=headers)
print(r, r.text)
import json

data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
data_json = json.dumps(data)
print(data_json)
import json


talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""
talaba = json.loads(talaba_json)
print(f"Talabaning ismi: {talaba['ism']}")
print(f"Talabaning familiyasi: {talaba['familiya']}")
print(f"Talabaning yili: {talaba['tyil']}")

with open('data.json','w') as f:
    json.dump(data,f)

with open('talaba.json','w') as f:
    json.dump(talaba,f)

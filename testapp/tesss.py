import requests
import json
BASE_URL = "http://127.0.0.1:8000/"
ENDPOINT =  "api/"
def get_resources(id=None):
    data = {}
    if id is not None:
        data={
            'id':id
        }
    resp = requests.get(BASE_URL + ENDPOINT,data = json.dumps(data))
    print(resp.status_code)
    print(resp.json())

get_resources()    


def create_resources():
    new_student = {
        'name':'adithya kashyap h m',
        'math': 74,
        'ddt':73,
        'dat':83,
        'ca':71,
        'dm':83,
        'op':84,
        'dd':94,
        'da':91,
        'es':43


    }
    r = requests.post(BASE_URL+ENDPOINT ,data = json.dumps(new_student))
    print(r.status_code)
    print(r.json())


#create_resources()    

def update_resources(id):
    new_student = {
        'id':id,
        'name': 'stalin',
        'da': 9,
        
      


    }
    r = requests.put(BASE_URL+ENDPOINT ,data = json.dumps(new_student))
    print(r.status_code)
    print(r.json())

#update_resources(5)    



def delete_resources(id):
    data = {
        'id':id,
    }
    r = requests.delete(BASE_URL+ENDPOINT,data = json.dumps(data))
    print(r.status_code)
    print(r.json())
#delete_resources(4)    
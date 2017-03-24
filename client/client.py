import requests
import time


UUID = "26a44c2e-e116-4219-a55b-63392a39265c"



content = {
        "id": UUID
    }

#request = requests.get("http://127.0.0.1:8000/api/hb")
#print(request.text)



def Main_loop():
    while True:
        requests.post("http://127.0.0.1:8000/api/hb", json=content)
        time.sleep(10)


try:
    Main_loop()
except KeyboardInterrupt:
    print('\n\nKeyboard exception received. Exiting.')
    exit()
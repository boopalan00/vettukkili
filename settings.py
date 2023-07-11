import os
import json



def history(url):
    if os.path.isfile('catch'+url):
        with open(url+'.json') as f:
            hf = json.load(f)
    else:
        hf = False
    return hf
     



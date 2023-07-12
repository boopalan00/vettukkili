import json
from argparse import ArgumentParser
from settings import history 


parse = ArgumentParser(description="*", epilog="----------")

parse.add_argument('-u','--url',dest='url',type=str,help='')
parse.add_argument('-h','--hty',dest='hty',type=str,help='')
parse.add_argument('-d','--dt',dest='dt',type=str,help='')

ags = parse.parse_args()

url = ags.url
hty = ags.hty.lower()
dt = ags.dt

if url:
    if url.startswith( ('http://','https://') ):
        print('valid url') 
    else:
        print("invalid url")
        exit() 

if hty in ['y','yes']:
    history(url)
else:
    hty = False




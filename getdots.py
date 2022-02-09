from PIL import Image
import requests
from io import BytesIO
import json
from time import sleep

metadataList = []

for i in range(0,10000):
    imageUrl = 'https://gateway.pinata.cloud/ipfs/QmVqMYxaEkifE7FoMkdNtryXhPNgHwA89msFQUBQbEYwKE/images/{}.png'.format(i)
    response = requests.get(imageUrl)
    img = Image.open(BytesIO(response.content))
    img.save(f"img/{i}.png", format='png')
    if (i%100 == 0):
        print("Sleeping after processing: {}".format(i))
        sleep(0.5)

with open('metadata.json', 'a') as f:
    for i in range(0,10000):
        metadataUrl = "https://dotdotdotnft.herokuapp.com/api/{}".format(i)
        response = requests.get(metadataUrl)
        metadataList.append(json.loads(response.text))
        f.write(response.text)
        if (i%100 == 0):
            print("Sleeping after processing: {}".format(i))
            sleep(1)

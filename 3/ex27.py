import aiohttp
import asyncio

async def getData(session, url):
    async with session.get(url) as resource:
        return await resource.text()

async def main():
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        data = await getData(session, 'http://github.com/rroszczyk/Python/raw/master/Pliki/alice.txt')
        print(len(data))

asyncio.run(main())


#import requests
#
#def pobierzPlik(url, nazwaPliku):
#    req = requests.get(url, stream=True)
#    with open(nazwaPliku, 'wb') as uchwytPliku:
#        for chunk in req.iter_content():
#            uchwytPliku.write(chunk)

#nazwyPlikow = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt', 'milionCyfrLiczbyPi.txt']
#for nazwa in nazwyPlikow:
#  pobierzPlik("https://github.com/rroszczyk/Python/raw/master/Pliki/"+nazwa, nazwa)
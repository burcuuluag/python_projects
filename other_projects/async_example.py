import asyncio

#ornek1
async def main():
    print('burcu')

asyncio.run(main())


#ornek2
async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')
    await asyncio.sleep(1)
    print('Burcu')

asyncio.run(main())


#ornek3
async def main():
    print('burcu')
    await foo('text')
    print('finished')

async def foo(text):
    print(text)
    await asyncio.sleep(1)

asyncio.run(main())


#ornek4
async def main():
    print('burcu')
    task = asyncio.create_task(foo('text'))
    await task
    print('finished')

async def foo(text):
    print(text)
    await asyncio.sleep(1)

asyncio.run(main())



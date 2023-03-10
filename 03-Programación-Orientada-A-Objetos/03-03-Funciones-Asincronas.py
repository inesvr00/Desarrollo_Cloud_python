# Ejecución asíncrona

import asyncio

async def main():
    await asyncio.gather(func1(), func2())

    
async def func1():
    for i in range(11):
        print(i)
        await asyncio.sleep(1)
        
async def func2():
    print("Hello...")
    await asyncio.sleep(5)
    print("... Mundo")
    
print("Inicio")
asyncio.run(main())
print("Fin")
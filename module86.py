#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     10-07-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------


#day 96
#asynclO in python- it means asynchronous behaviour

import time
import asyncio
async def function1():
    await asyncio.sleep(1)
    print("func 1")
async def function2():
    await asyncio.sleep(1)
    print("func 2")
async def function3():
    await asyncio.sleep(4)
    print("func 3")

async def main():
    L = await asynco.gather(
    function1(),
    function2(),
    function3(),
    )
    print(L)
   # task=asyncio.create_task(function1())
    #await function1()
    #await function2()
    #await function3()

#asyncio.run((main))


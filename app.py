# import asyncio
# import signal
# import os

# import websockets


# async def echo(websocket):
#     async for message in websocket:
#         await websocket.send(message)


# async def main():
#     # Set the stop condition when receiving SIGTERM.
#     loop = asyncio.get_running_loop()
#     stop = loop.create_future()
#     loop.add_signal_handler(signal.SIGTERM, stop.set_result, None)

#     async with websockets.serve(
#         echo,
#         host="",
#         port=int(os.environ["PORT"]),
#     ):
#         await stop


# if __name__ == "__main__":
#     asyncio.run(main())

import asyncio
import signal
import json
import websockets
from all_vuln_one_var import run_program
import os

async def hello():  # put application's code here
    await run_program()
    return json({'about': "Hello world"})

async def echo(websocket):
    async for message in websocket:
        print(message)
        message=message.split(" ")
        if message[0] == "start":
            final_message = run_program(message[1])
            print("jjj",final_message)

        await websocket.send(json.dumps(final_message))

async def main():
    # Set the stop condition when receiving SIGTERM.
    loop = asyncio.get_running_loop()
    stop = loop.create_future()
    loop.add_signal_handler(signal.SIGTERM, stop.set_result, None)

    async with websockets.serve(
        echo,
        host="",
        port=int(os.environ["PORT"]),
    ):
        await stop

if __name__ == "__main__":
    asyncio.run(main())

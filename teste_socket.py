import asyncio
import socketio

sio = socketio.AsyncClient()

@sio.event
async def connect():
    print('connection established')
    while True:
        await emit_sensor_event()

async def emit_sensor_event():
    await sio.emit('sensor', "testando")
    await asyncio.sleep(1)  # Optional: Add a delay between emits


@sio.event
async def disconnect():
    print('disconnected from server')

async def main():
    await sio.connect('http://150.162.217.34:3001')
    await sio.wait()

if __name__ == '__main__':
    asyncio.run(main())

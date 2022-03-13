import asyncio

async def echo(reader, writer):
    data = await reader.read(1000)
    message = data.decode()
    addr = writer.get_extra_info('peername')
    print(f"Odebrano wiadomość: {message} from {addr}")

    print(f"Wiadomość: {message} została odesłana")
    writer.write(data)
    await writer.drain()

    print("Zamykamy połączenie")
    writer.close()


lp = asyncio.new_event_loop()
connection = asyncio.start_server(echo, "127.0.0.1", 8888, loop=lp)
server = lp.run_until_complete(connection)

print(f"Serwer został uruchomiony na {server.sockets[0].getsocketname()}")
try:
    lp.run_forever()
except KeyboardInterrupt:
    pass

server.close()
lp.run_until_complete(server.wait_closed())
lp.close()
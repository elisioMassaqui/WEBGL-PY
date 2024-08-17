import asyncio
import websockets

clients = set()  # Para manter o controle dos clientes conectados

async def handle_client(websocket, path):
    # Adiciona o cliente à lista
    clients.add(websocket)
    try:
        async for message in websocket:
            print(f"Recebido: {message}")
            # Cria uma lista de tarefas para enviar a mensagem para todos os clientes
            tasks = [client.send(message) for client in clients]
            await asyncio.gather(*tasks)  # Aguarda todas as tarefas serem concluídas
    except websockets.ConnectionClosed:
        print("Cliente desconectado")
    finally:
        # Remove o cliente da lista
        clients.remove(websocket)

async def main():
    async with websockets.serve(handle_client, "localhost", 8765):
        await asyncio.Future()  # Run forever

asyncio.run(main())

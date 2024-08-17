const WebSocket = require('ws');

const wss = new WebSocket.Server({ port: 8765 });

wss.on('connection', (ws) => {
    console.log('Cliente WebGL conectado');

    ws.on('message', (message) => {
        console.log('Mensagem recebida do cliente WebGL:', message);
    });

    ws.on('close', () => {
        console.log('Cliente WebGL desconectado');
    });
});

console.log('Servidor WebSocket rodando na porta 8765');

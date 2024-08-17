const WebSocket = require('ws');

const wss = new WebSocket.Server({ port: 8765 });

const messages = ["Hello, Unity!", "Message 2", "Message 1", "Message 3", "Another Message"];

wss.on('connection', (ws) => {
  setInterval(() => {
    const randomMessage = messages[Math.floor(Math.random() * messages.length)];
    ws.send(randomMessage);
  }, 1000);
});
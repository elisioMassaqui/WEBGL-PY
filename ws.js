const WebSocket = require('ws');

const wss = new WebSocket.Server({ port: 8765 });

const messages = ["Hello, Unity!", "Another Message", "Hello, Unity!", "Message 2", "Message 3", "Message 1", "Message 1"];

wss.on('connection', (ws) => {
  setInterval(() => {
    const randomMessage = messages[Math.floor(Math.random() * messages.length)];
    console.log(messages)
    ws.send(randomMessage);
  }, 1000);
});
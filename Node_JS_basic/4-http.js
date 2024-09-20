const http = require('http');

const app = http.createServer((request, result) => {
  result.writeHead(200, { 'Content-Type': 'text/plain' });
  result.write('Hello Holberton School!');
  result.end();
});

const PORT = 1245;
const HOST = 'localhost';

app.listen(PORT, HOST, () => {});

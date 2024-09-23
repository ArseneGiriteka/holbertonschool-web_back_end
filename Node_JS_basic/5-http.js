const promise = require('fs').promises;
const http = require('http');

async function countStudents(path) {
  let result = '';
  try {
    const data = await promise.readFile(path, 'utf-8');
    const rows = data.trim().split('\n');
    rows.shift();
    result += `Number of students: ${rows.length}`;

    const fields = [];

    for (let i = 0; i < rows.length; i += 1) {
      const field = rows[i].split(',')[3].trim();
      if (!(fields.includes(field))) {
        fields.push(field);
      }
    }

    for (const field of fields) {
      const names = [];
      for (const row of rows) {
        if (field === row.trim().split(',')[3].trim()) {
          names.push(row.trim().split(',')[0].trim());
        }
      }

      let strNames = '';
      for (let i = 0; i < names.length; i += 1) {
        if (names.length === 0) {
          strNames = '';
        } else if (i !== names.length - 1) {
          strNames += ` ${names[i]},`;
        } else {
          strNames += ` ${names[i]}`;
        }
      }
      result += `\nNumber of students in ${field}: ${names.length}. List:${strNames}`;
    }
  } catch (error) {
    throw new Error('Error: Cannot load the database');
  }
  return result;
}

const app = http.createServer(async (req, res) => {
  const { url } = req;

  res.setHeader('Content-Type', 'text/plain');
  if (url === '/') {
    res.statusCode = 200;
    res.end('Hello Holberton School!');
  } else if (url === '/students') {
    const database = process.argv[2];
    if (!database) {
      res.statusCode = 500;
      res.end('Error: Cannot load the database');
    } else {
      try {
        const data = await countStudents(database);
        res.statusCode = 200;
        res.end(`This is the list of our students\n${data}`);
      } catch (error) {
        res.statusCode = 500;
        res.end(error.message);
      }
    }
  } else {
    res.statusCode = 404;
    res.end('404 Not Found');
  }
});

const PORT = 1245;

app.listen(PORT, () => {
  console.log(`Server is listening on port ${PORT}/`);
});

module.exports = app;
module.exports = countStudents;

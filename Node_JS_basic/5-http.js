const promise = require('fs').promises;
const http = require('http');

async function countStudents(path) {
  let result = '';
  try {
    const data = await promise.readFile(path, 'utf-8');
    const rows = data.trim().split('\n');
    rows.shift();
    // console.log(`Number of students: ${rows.length}`);
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
      // console.log(`Number of students in ${field}: ${names.length}. List:${strNames}`);
      result += `\nNumber of students in ${field}: ${names.length}. List:${strNames}`;
    }
  } catch (error) {
    return 'Error: Cannot load the database';
  }
  return result;
}

const app = http.createServer(async (req, res) => {
  const { url } = req;

  if (url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.write('Hello Holberton School!');
    res.end();
  } else if (url === '/students') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.write('This is the list of our students\n');
    res.write(await countStudents(process.argv[2]));
    res.end();
  } else {
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.write('Error 404 : Page Not Found');
    res.end();
  }
});

const PORT = 1245;

app.listen(PORT, () => {
  // console.log(`Server is listening on port ${PORT}/`);
});

module.exports = app;
module.exports = countStudents;

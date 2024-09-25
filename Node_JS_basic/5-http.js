const http = require('http');
const fs = require('fs');
const path = require('path');
const { parse } = require('csv-parse');

const countStudents = async (database) => {
  return new Promise((resolve, reject) => {
    let data = '';
    const studentsByField = {};

    const parser = fs.createReadStream(database)
      .pipe(parse({ delimiter: ',', from_line: 2 }));

    parser.on('data', (row) => {
      if (row.length > 0 && row[0].trim()) {
        const field = row[3]; // Assuming that field is at index 3
        if (!studentsByField[field]) {
          studentsByField[field] = [];
        }
        studentsByField[field].push(row[0]);
      }
    });

    parser.on('end', () => {
      let totalStudents = 0;
      let output = '';

      for (const field in studentsByField) {
        const studentCount = studentsByField[field].length;
        totalStudents += studentCount;
        output += `Number of students in ${field}: ${studentCount}. List: ${studentsByField[field].join(', ')}\n`;
      }

      resolve(`Number of students: ${totalStudents}\n` + output.trim());
    });

    parser.on('error', (err) => {
      reject(new Error(`Cannot load the database ${database}`));
    });
  });
};

const app = http.createServer(async (req, res) => {
  const { url } = req;

  if (url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.write('Hello Holberton School!');
    res.end();
  } else if (url === '/students') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.write('This is the list of our students\n');
    try {
      const result = await countStudents(process.argv[2]);
      res.write(result);
    } catch (error) {
      res.write(error.message);
    }
    res.end();
  } else {
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.write('Error 404: Page Not Found');
    res.end();
  }
});

const PORT = 1245;
app.listen(PORT, () => {
  console.log(`Server is listening on port ${PORT}/`);
});

module.exports = { app, countStudents };

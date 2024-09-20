const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf-8');
    const rows = data.trim().split('\n');
    rows.shift();
    console.log(`Number of students: ${rows.length}`);

    const fields = [];

    for (let i = 0; i < rows.length; i += 1) {
      const field = rows[i].split(',')[3];
      if (!(fields.includes(field))) {
        fields.push(field);
      }
    }

    for (const field of fields) {
      const names = [];
      for (const row of rows) {
        if (field === row.trim().split(',')[3].trim()) {
          names.push(row.trim().split(',')[0]);
        }
      }

      let strNames = '';
      for (let i = 0; i < names.length; i += 1) {
        if (i !== names.length - 1) {
          strNames += ` ${names[i]},`;
        } else {
          strNames += ` ${names[i]}`;
        }
      }

      console.log(`Number of students in ${field}: ${names.length}. List:${strNames}`);
    }
  } catch (error) {
    console.log('Cannot load the database');
  }
}

module.exports = countStudents;

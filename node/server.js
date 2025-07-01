require('dotenv').config();
const express = require('express');
const { spawn } = require('child_process');
const path = require('path');

const PY = 'py';
const SCRIPT = path.join(__dirname, '../python/enumerate.py');

const app = express();
app.get('/enum/:domain', (req, res) => {
  const py = spawn(PY, [SCRIPT, req.params.domain]);
  let out = "", err = "";

  py.stdout.on('data', d => out += d);
  py.stderr.on('data', d => err += d);

  py.on('close', code => {
    if (code !== 0 || err) {
      return res.status(500).json({ error: err || `Exit code ${code}` });
    }
    try {
      return res.json(JSON.parse(out));
    } catch {
      return res.status(500).json({ error: 'Invalid JSON from Python' });
    }
  });
});

const PORT = 8000;
app.listen(PORT, () => console.log(`Server on http://localhost:${PORT}`));

// index.js
// where your node app starts

// Initialize the project
require('dotenv').config();
const express = require('express');
const app = express();

// Enable CORS (https://en.wikipedia.org/wiki/Cross-origin_resource_sharing)
// Allow all origins for testing. You can restrict this based on your needs.
const cors = require('cors');
app.use(cors());

// Serve static files from the 'public' directory
app.use(express.static('public'));

// Define basic routing
app.get('/', function (req, res) {
  res.sendFile(__dirname + '/views/index.html');
});

// Define an API endpoint to get information about the client
app.get('/api/whoami', function (req, res) {
  const ipaddress = req.ip; // Use req.ip to get client IP address
  const language = req.headers['accept-language'];
  const software = req.headers['user-agent'];

  res.json({
    ipaddress,
    language,
    software
  });
});

// Start the server and listen for requests
const PORT = process.env.PORT || 3000;
const server = app.listen(PORT, function () {
  console.log('Your app is listening on port ' + PORT);
});

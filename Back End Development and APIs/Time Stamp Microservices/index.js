const express = require('express');
const app = express();
const cors = require('cors');

app.use(cors({ optionsSuccessStatus: 200 }));
app.use(express.static('public'));

app.get("/", (req, res) => {
  res.sendFile(__dirname + '/views/index.html');
});

// Helper function to check if a date is valid
const isInvalidDate = (date) => date.toUTCString() === "Invalid Date";

// API endpoint for handling date requests
const handleDateRequest = (req, res) => {
  let date = new Date(req.params.date);

  if (isInvalidDate(date)) {
    date = new Date(+req.params.date);
  }

  if (isInvalidDate(date)) {
    res.json({ error: "Invalid Date" });
    return;
  }

  res.json({
    unix: date.getTime(),
    utc: date.toUTCString(),
  });
};

app.get("/api/:date", handleDateRequest);

// Default API endpoint for current time
app.get("/api", (req, res) => {
  const currentTime = new Date();
  res.json({
    unix: currentTime.getTime(),
    utc: currentTime.toUTCString(),
  });
});

const PORT = process.env.PORT || 3000;
const listener = app.listen(PORT, () => {
  console.log('Your app is listening on port ' + PORT);
});

const express = require('express');
const app = express();
const cors = require('cors');
require('dotenv').config();
const mongoose = require('mongoose');

// Database connection
mongoose.connect(process.env.DB_URL);

// Define schemas and models
const userSchema = new mongoose.Schema({
  username: String,
});
const User = mongoose.model('User', userSchema);

const exerciseSchema = new mongoose.Schema({
  user_id: { type: String, required: true },
  description: String,
  duration: Number,
  date: Date,
});
const Exercise = mongoose.model('Exercise', exerciseSchema);

// Middleware
app.use(cors());
app.use(express.static('public'));
app.use(express.json()); // Parse JSON request bodies

// Routes
app.get('/', (req, res) => {
  res.sendFile(__dirname + '/views/index.html');
});

app.get('/api/users', async (req, res) => {
  try {
    const users = await User.find({}).select('_id username');
    res.json(users);
  } catch (err) {
    console.error(err);
    res.status(500).send('Error fetching users');
  }
});

app.post('/api/users', async (req, res) => {
  try {
    const { username } = req.body;
    const user = new User({ username });
    await user.save();
    res.json(user);
  } catch (err) {
    console.error(err);
    res.status(500).send('Error creating user');
  }
});

app.post('/api/users/:_id/exercises', async (req, res) => {
  try {
    const id = req.params._id;
    const { description, duration, date } = req.body;
    const user = await User.findById(id);

    if (!user) {
      return res.status(404).send('User not found');
    }

    const exercise = new Exercise({
      user_id: user._id,
      description,
      duration,
      date: date ? new Date(date) : new Date(),
    });

    await exercise.save();

    res.json({
      _id: user._id,
      username: user.username,
      description: exercise.description,
      duration: exercise.duration,
      date: exercise.date.toDateString(),
    });
  } catch (err) {
    console.error(err);
    res.status(500).send('Error saving exercise');
  }
});

app.get('/api/users/:_id/logs', async (req, res) => {
  try {
    const { from, to, limit } = req.query;
    const id = req.params._id;
    const user = await User.findById(id);

    if (!user) {
      return res.status(404).send('User not found');
    }

    const dateFilter = {};
    if (from) {
      dateFilter.$gte = new Date(from);
    }
    if (to) {
      dateFilter.$lte = new Date(to);
    }

    const exerciseFilter = {
      user_id: id,
    };
    if (from || to) {
      exerciseFilter.date = dateFilter;
    }

    const exercises = await Exercise.find(exerciseFilter).limit(+limit || 500);

    const log = exercises.map(e => ({
      description: e.description,
      duration: e.duration,
      date: e.date.toDateString(),
    }));

    res.json({
      username: user.username,
      count: exercises.length,
      _id: user._id,
      log,
    });
  } catch (err) {
    console.error(err);
    res.status(500).send('Error fetching exercise logs');
  }
});

// Start the server
const port = process.env.PORT || 3000;
const listener = app.listen(port, () => {
  console.log('Your app is listening on port ' + port);
});

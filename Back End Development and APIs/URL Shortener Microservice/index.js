require('dotenv').config();
const express = require('express');
const cors = require('cors');
const app = express();
const { MongoClient } = require('mongodb');
const dns = require('dns');
const urlparser = require('url');

const port = process.env.PORT || 3000;

app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use('/public', express.static(`${process.cwd()}/public`));

app.get('/', (req, res) => {
  res.sendFile(process.cwd() + '/views/index.html');
});

const performDnsLookup = (url) => {
  return new Promise((resolve, reject) => {
    dns.lookup(urlparser.parse(url).hostname, (err, address) => {
      if (err || !address) {
        reject(new Error("Invalid URL"));
      } else {
        resolve();
      }
    });
  });
};

(async () => {
  const client = new MongoClient(process.env.DB_MAIN);
  try {
    await client.connect();
    const db = client.db("urlshortener");
    const urls = db.collection("session");

    app.post('/api/shorturl', async (req, res) => {
      const url = req.body.url;
      
      try {
        await performDnsLookup(url);
        
        const urlCount = await urls.countDocuments({});
        const urlDoc = {
          url: url,
          short_url: urlCount
        };

        const result = await urls.insertOne(urlDoc);
        console.log(result);

        res.json({ original_url: url, short_url: urlCount });
      } catch (error) {
        res.json({ error: error.message });
      }
    });

    app.get("/api/shorturl/:short_url", async (req, res) => {
      const shorturl = req.params.short_url;
      const urlDoc = await urls.findOne({ short_url: +shorturl });

      if (urlDoc) {
        res.redirect(urlDoc.url);
      } else {
        res.json({ error: "Short URL not found" });
      }
    });

    app.listen(port, () => {
      console.log(`Listening on port ${port}`);
    });
  } catch (err) {
    console.error("Error connecting to MongoDB:", err);
  }
})();

const express = require('express')
const cors = require('cors');
const path = require('path')
const moment = require('moment')
const { HOST } = require('./src/constants')
const db = require('./src/database')

const PORT = process.env.PORT || 3000


const allowedOrigins = [/.*localhost.*/, /.*cryptokeule.tokents.org*/];


const app = express()
  .set('port', PORT)
  .set('views', path.join(__dirname, 'views'))
  .set('view engine', 'ejs')

app.use(cors({
    origin: allowedOrigins,
}));

// Static public files
app.use(express.static(path.join(__dirname, 'public')))

app.get('/', function(req, res) {
  res.send('200');
})

app.get('/entree/:token_id', function(req, res) {
  const tokenId = parseInt(req.params.token_id).toString();
  var entJson = `public/entree/json/${tokenId}.json`
  res.header("Content-Type",'application/json');
  res.sendFile(path.join(__dirname, entJson));
})

app.listen(app.get('port'), function() {
  console.log('Node app is running on port', app.get('port'));
})

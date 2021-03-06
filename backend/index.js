const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const routers = require('./routers');
const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));
app.use(cors());
app.use('/', routers);


const port = process.env.PORT || 8000;
app.listen(port, console.log(`listen to ${port}`));


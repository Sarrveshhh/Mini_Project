const express = require('express');
const dotenv = require('dotenv').config();
const request = require('request');
const port = process.env.PORT || 8000;

const app = express();

app.use(express.json());
app.use(express.urlencoded({extended: false}));
app.use(express.raw())


app.post('/predict', (req, res) => {
    request('http://127.0.0.1:5000/predict', function (error, response, body) {
        console.error('error:', error); 
        console.log('body:', body);
        res.send(body);
    });
});
app.listen(port, () => {
    console.log(`listening on port ${port}`);
});

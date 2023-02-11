const express = require('express');
const dotenv = require('dotenv').config();
const request = require('request');
const port = process.env.PORT || 5000;

const app = express();

app.get('/api/goals', (req, res) => {
    res.send('Get goals');
})
app.listen(port, () => {
    console.log(`listening on port ${port}`);
})

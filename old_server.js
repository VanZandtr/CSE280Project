
var express = require("express");
var mapRouter = require("./Routes/mapRouter");
var imageRouter = require("./Routes/imageRouter");
var pathRouter = require("./Routes/pathRouter");
var bodyParser = require("body-parser");
var mongoose = require("mongoose");
var MongoClient = require('mongodb').MongoClient;
const path = require("path");


const db = mongoose.connect("mongodb+srv://vanzandtr:vanzandtr@cluster0-gomra.mongodb.net/mapsDatabase?retryWrites=true", 
function(err, db)
{
    if (err) {
        console.log('Unable to connect to the server. Please start the server. Error:', err);
    } else {
        console.log('Connected to Server successfully!');
    }
});

const app = express();
const port = process.env.PORT || 5656;

app.use(express.static("static"));
app.use(express.static("templates"));

app.use(bodyParser.json({ limit:'100mb'}));
app.use(bodyParser.urlencoded({ limit:'100mb', extended: true}));
app.use('/api/maps', mapRouter);
app.use('/api/images', imageRouter);
app.use('/api/path', pathRouter);


app.listen(port, () => {
    console.log(`http://localhost:${port}`)
})
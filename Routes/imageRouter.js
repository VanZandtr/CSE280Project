var express = require('express');
var Image = require('../models/imageModel');
var mongoose = require('mongoose')

const fs = require('fs');
const path = require('path');
const uploadDir = ''; // uploading the file to the same path as app.js

const imageRouter = express.Router();

imageRouter.route('/')
    .get((req, res) => {
        Image.find({}, (err, images) => {
            res.json(images);
        })
    })

imageRouter.use('/:imageId', (req, res, next)=>{
    Image.findById(req.params.imageId, (err,image)=>{
        if(err)
            res.status(500).send(err);
        else {
            //set the found image == req.image
            req.image = image;
            next()
        }
    })
})
imageRouter.route('/:imageId')
    .get((req, res) => {
        //--------------------------------
        //write req.image.imageData to file
        fs.writeFile(req.image.imageName + ".txt", req.image.imageData, (err) => {
            if(err)
                res.status(500).send(err);
        });

        //spawn child process
        var spawn = require("child_process").spawn;

        //have process execute convert map.txt (compressed) -------> map.bmp (decompressed)
        var process = spawn('python', ["./map_compress_decompress.py",
                                req.image.imageName,
                                req.image.imageName]);
        
        //send image                                
        process.stdout.on('data', function(data){
            res.send(data);
        })                                
        //--------------------------------

        //send the found image.data to the user
        res.send(req.image.imageData);
        //res.json(req.image);
    })
    
module.exports = imageRouter;
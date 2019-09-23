var express = require('express');
var Image = require('../models/imageModel');
var mongoose = require('mongoose')
//const formidable = require('formidable');
const path = require('path');
const uploadDir = ''; // uploading the file to the same path as app.js
const imageRouter = express.Router();

imageRouter.route('/')
    .get((req, res) => {
        Image.find({}, (err, images) => {
            res.json(images);
        })
    })

imageRouter.use('/:imageName', (req, res, next)=>{
    Image.findById(req.params.imageId, (err,image)=>{
        if(err)
            res.status(500).send(err);
        else {
            req.image = image;
            next()
        }
    })
})
imageRouter.route('/:imageName')

    .get((req, res) => {
        res.json(req.image.imageData)
    })
    
module.exports = imageRouter;
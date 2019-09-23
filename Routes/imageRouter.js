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

imageRouter.use('/name/:imageName', (req, res, next)=>{
    Image.findById(req.image.imageId, (err,image)=>{
        if(err)
            res.status(500).send(err);
        else {
            res.send(image.imageData);
            next()
        }
    })
})
/*
imageRouter.route('/id/:Id')

    .get((req, res) => {
        res.json(req.image.imageData)
    })

    .put((req,res) => {
        req.image.imageName = req.body.imageName;
        req.image.imageData= req.body.imageData;
        req.image.save()
        res.json(req.image)
    })
*/
module.exports = imageRouter;
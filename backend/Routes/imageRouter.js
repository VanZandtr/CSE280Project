var express = require('express');
var Image = require('../models/imageModel');
var mongoose = require('mongoose')
const formidable = require('formidable');
const path = require('path');
const uploadDir = ''; // uploading the file to the same path as app.js
const imageRouter = express.Router();

imageRouter.route('/')
    .get((req, res) => {
        Image.find({}, (err, images) => {
            res.json(images)
        })
    })

    .post((req, res) => {
        let image = new Image(req.body)
        image.save();
        res.status(201).send(image)
    })

/*
	var form = new formidable.IncomingForm();

	form.parse(req);

    	form.on('fileBegin', function (name, file){
        	file.path = file.name;
    	});

    	form.on('file', function (name, file){
        	console.log('Uploaded ' + file.name);
    	});

    	res.sendFile(form);
    })
*/
/*
       var form = new formidable.IncomingForm()
       form.multiples = true
       form.keepExtensions = true
       form.uploadDir = uploadDir
       form.parse(req, (err, fields, files) => {
       if (err) return res.status(500).json({ error: err })
	 console.log(err)
         res.status(200).json({ uploaded: true })
       })
       form.on('fileBegin', function (name, file) {
         console.log(name)
         console.log(file)

         const [fileName, fileExt] = file.name.split('.')
         file.path = path.join(uploadDir, `${fileName}_${new Date().getTime()}.${fileExt}`)
       })
       res.status(201).send(form)
*/



imageRouter.use('/:imageName', (req, res, next)=>{
    console.log(mongoose.Types.ObjectId.isValid(req.toString()))
    Image.findById(req.params.imageId, (err,image)=>{
        if(err)
            res.status(500).send(err)
        else {
            req.image = image;
            next()
        }
    })
})

imageRouter.route('/:imageId')

    .get((req, res) => {
        res.json(req.image)
    })

    .put((req,res) => {
        req.image.imageName = req.body.imageName;
        req.image.imageData= req.body.imageData;
        req.image.save()
        res.json(req.image)
    })
    .patch((req,res)=>{
        if(req.body._id){
            delete req.body._id;
        }
        for( let p in req.body ){
            req.image[p] = req.body[p]
        }
        req.image.save()
        res.json(req.image)
    }) //patch
    .delete((req,res)=>{
        req.image.remove(err => {
            if(err){
                res.status(500).send(err)
            }
            else{
                res.status(204).send('removed')
            }
        })
    }) //delete


module.exports = imageRouter;
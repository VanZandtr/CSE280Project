var express = require('express');
var Map = require('../models/mapModel');
var fs = require('fs');

const mapRouter = express.Router();

mapRouter.route('/')
    .get((req, res) => {
        Map.find({}, (err, maps) => {
            res.json(maps)
        })
    })

mapRouter.use('/:mapId', (req, res, next)=>{
   Map.findById(req.params.mapId, (err,map)=>{
        if(err)
            res.status(500).send(err)
        else {
            req.map = map;
            next()
        }
    })
})

mapRouter.route('/:mapId')
    .get((req, res) => {
        res.json(req.map)
    })

module.exports = mapRouter;

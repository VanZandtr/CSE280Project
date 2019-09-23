var express = require('express');
var Map = require('../models/mapModel');
var fs = require('fs');

//import express from 'express';
//import Map from '../models/mapModel';

const mapRouter = express.Router();

mapRouter.route('/')
    .get((req, res) => {
        Map.find({}, (err, maps) => {
            res.json(maps)
        })
    })
    .post((req, res) => {
        let map = new Map(req.body)
        map.save();
        res.status(201).send(map)
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
    .put((req,res) => {
        req.map.mapName = req.body.mapName;
        req.map.imagePath= req.body.imagePath;
        req.map.save()
        res.json(req.map)
    })
    .patch((req,res)=>{
        if(req.body._id){
            delete req.body._id;
        }
        for( let p in req.body ){
            req.map[p] = req.body[p]
        }
        req.map.save()
        res.json(req.map)
    })//patch
    .delete((req,res)=>{
        req.map.remove(err => {
            if(err){
                res.status(500).send(err)
            }
            else{
                res.status(204).send('removed')
            }
        })
    }) //delete

//export default mapRouter;
module.exports = mapRouter;

var express = require('express');
var Path = require('../models/pathModel');
var fs = require('fs');

const pathRouter = express.Router();

/**
map_filename - pgm for map
start        - x,y pair for start
end          - x,y pair for end
*/
function mapPGM(map_filename, start, end) {
    const out_filename = map_filename.replace('.pgm', '_' + start + '_' + end + '.pgm');
    const spawn = require("child_process").spawn;
    const pythonProcess = spawn('python2.7',["A-star/a-star.py", map_filename, out_filename, start, end]);
    return out_filename;
}

pathRouter.route('/')
    .get((req, res) => {
	// TODO: Get parameters (filename, start_pos, end_pos) from request
	var filename = 'packard_4thfloor.pgm';
	var start_pos = '592,120';
	var end_pos   = '540,1524';
        var map_filename = mapPGM(filename, start_pos, end_pos);
        res.json({'map_filename': map_filename})
    })

//export default mapRouter;
module.exports = pathRouter;

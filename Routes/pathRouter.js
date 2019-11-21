var express = require('express');
var Path = require('../models/pathModel');
var fs = require('fs');

const pathRouter = express.Router();

/**
map_filename - pgm for map
start        - x,y pair for start
end          - x,y pair for end
*/
function mapPGM(map_filename, out_filename, start, end) {
    const spawn = require("child_process").spawn;
    const pythonProcess = spawn('python2.7',["A-star/a-star.py", map_filename, out_filename, start, end]);
    return pythonProcess;
}
function getMap(map_filename, start_pos, end_pos, res) {
    const out_filename = map_filename.replace('.pgm', '_' + start_pos + '_' + end_pos + '.pgm');
    const png_filename = out_filename.replace('.pgm', '.png');
    fs.exists(png_filename, function(exists) {
        if(exists) {
            console.log('Requested path exists, returning cached copy');
            res.writeHead(200, {
                "Content-Type": "image/x-portable-bitmap",
            });
            fs.createReadStream(png_filename).pipe(res);
        } else {
            console.log('Requested path doesn\'t exist, mapping now...');
            var proc = mapPGM(map_filename, out_filename, start_pos, end_pos);
            proc.stdout.on('data', (data) => {
                getMap(map_filename, start_pos, end_pos, res);
            });
        }
    });
} 

// TODO: Temporary here until mapping implemented in the database
const room_mapping = {
    'packard-202': '592,120',
    'packard-262': '540,1524',
};
const building_mapping = {
    'packard-4': 'packard_4thfloor.pgm',
    'packard-2': 'packard_2ndfloor.pgm'
};

pathRouter.route('/')
    .get((req, res) => {
    	//var filename = 'packard_4thfloor.pgm';
    	//var start_pos = '592,120';
    	//var end_pos   = '540,1524';
        var building_start = building_mapping[req.query.building_start];
        var start_loc      = room_mapping[req.query.room_start];
        var end_loc        = room_mapping[req.query.room_end];
        
        if(typeof building_start == 'undefined' || typeof start_loc == 'undefined' || typeof end_loc == 'undefined') {
            console.log('Unknown mapping locations for path detected');
            res.status(400);
            res.end('');
        } else {
            getMap(building_start, start_loc, end_loc, res);
        }
    })

//export default mapRouter;
module.exports = pathRouter;
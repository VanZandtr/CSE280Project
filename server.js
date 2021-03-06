const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');
const crypto = require('crypto');
const mongoose = require('mongoose');
const multer = require('multer');
const GridFsStorage = require('multer-gridfs-storage');
const Grid = require('gridfs-stream');
const methodOverride = require('method-override');
const fs = require('fs');
const app = express();

// Middleware
app.use(bodyParser.json());
app.use(methodOverride('_method'));
app.set('view engine', 'ejs');

// Mongo URI
const mongoURI = 'mongodb+srv://vanzandtr:vanzandtr@cluster0-gomra.mongodb.net/mapsDatabase';

// Create mongo connection
const conn = mongoose.createConnection(mongoURI);

// Init gfs
let gfs;

conn.once('open', () => {
  // Init stream
  gfs = Grid(conn.db, mongoose.mongo);
  gfs.collection('uploads');
});

// Create storage engine
const storage = new GridFsStorage({
  url: mongoURI,
  file: (req, file) => {
    return new Promise((resolve, reject) => {
      crypto.randomBytes(16, (err, buf) => {
        if (err) {
          return reject(err);
        }
        const filename = buf.toString('hex') + path.extname(file.originalname);
        const fileInfo = {
          filename: filename,
          bucketName: 'uploads'
        };
        resolve(fileInfo);
      });
    });
  }
});
const upload = multer({ storage });

// @route GET /
// @desc Loads form

app.use(express.static('views'));

app.get('/', (req, res) => {
   res.render('index');
});

app.get('/path/:from/:to', (req, res) => {
  if(req.params.from && req.params.to){
    //run pyton code with params --> board_out.pgm
    var spawn = require("child_process").spawn;

    //get building intials
    var building = (req.params.from).substring(0,2);
    console.log(building);

    //get room number from "from"
    var room_number = (req.params.from).substring(2);
    console.log(room_number);

    var first_number = room_number.substring(0,1);
    console.log(first_number);

    //roomabbr.roomnumber -------> (pa202, pa203)
    try{
	    var process = spawn('python', [path.join("pgm", "pgm.py"), path.join("maps", building, first_number, "path.pgm"), path.join("maps", building, first_number, first_number + ".pgm"), req.params.from, req.params.to]);
    }
    catch(e){
	    console.log(e);
	    var process = spawn('python', [path.join("../","pgm", "pgm.py"), path.join("../","maps", building, first_number, "path.pgm"), path.join("../", "maps", building, first_number, first_number + ".pgm"), req.params.from, req.params.to]);
    }


    process.stdout.on('data', function(data) {
	console.log('stdout: ' + data);
    });

    process.stderr.on('data', function(data) {
	console.log('stderr: ' + data);
    });

    setTimeout(function(){
	console.log("ending timeout");
    	//check if file exists
	try{
    if(fs.existsSync('./board_out.png')){
      res.sendFile('./board_out.png', { root: __dirname });  
    }
	}
	catch(err){
	    res.redirect('/');
	}
    }, 15000);
  }
  else{
    res.redirect('/');
  }
});

app.get('/views', (req, res) => {
  gfs.files.find().toArray((err, files) => {
    // Check if files
    if (!files || files.length === 0) {
      res.render('file_interface', { files: false });
    } else {
      files.map(file => {
        if (
          file.contentType === 'image/jpeg' ||
          file.contentType === 'image/png'
        ) {
          file.isImage = true;
        } else {
          file.isImage = false;
        }
      });
      res.render('file_interface', { files: files });
    }
  });
});

// @route POST /upload
// @desc  Uploads file to DB
app.post('/upload', upload.single('file'), (req, res) => {
  // res.json({ file: req.file });
  res.redirect('/');
});

// @route GET /files
// @desc  Display all files in JSON
app.get('/files', (req, res) => {
  gfs.files.find().toArray((err, files) => {
    // Check if files
    if (!files || files.length === 0) {
      return res.status(404).json({
        err: 'No files exist'
      });
    }

    // Files exist
    return res.json(files);
  });
});

// @route GET /files/:filename
// @desc  Display single file object
app.get('/files/:filename', (req, res) => {
  gfs.files.findOne({ filename: req.params.filename }, (err, file) => {
    // Check if file
    if (!file || file.length === 0) {
      return res.status(404).json({
        err: 'No file exists'
      });
    }
    // File exists
    return res.json(file);
  });
});

// @route GET /image/:filename
// @desc Display Image
app.get('/image/:filename', (req, res) => {
  gfs.files.findOne({ filename: req.params.filename }, (err, file) => {
    // Check if file
    if (!file || file.length === 0) {
      return res.status(404).json({
        err: 'No file exists'
      });
    }

    // Check if image
    if (file.contentType === 'image/jpeg' || file.contentType === 'image/png') {
      // Read output to browser
      const readstream = gfs.createReadStream(file.filename);
      readstream.pipe(res);
    } else {
      res.status(404).json({
        err: 'Not an image'
      });
    }
  });
});

// @route DELETE /files/:id
// @desc  Delete file
app.delete('/files/:id', (req, res) => {
  gfs.remove({ _id: req.params.id, root: 'uploads' }, (err, gridStore) => {
    if (err) {
      return res.status(404).json({ err: err });
    }

    res.redirect('/');
  });
});

app.set( 'port', ( process.env.PORT || 5000 ));

// Start node server
app.listen( app.get( 'port' ), function() {
  console.log( 'Node server is running on port ' + app.get( 'port' ));
});

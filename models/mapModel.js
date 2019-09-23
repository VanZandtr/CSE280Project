var mongoose = require('mongoose');

const Schema = mongoose.Schema;
const mapModel = new Schema({
    mapName: { type: String   },
    imagePath: { type: String }
})
module.exports = mongoose.model('maps', mapModel)

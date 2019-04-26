var mongoose = require('mongoose');

const Schema = mongoose.Schema;
const imageModel = new Schema({
    imageName: { type: String },
    imageData: { type: String }
})
module.exports = mongoose.model('images', imageModel)

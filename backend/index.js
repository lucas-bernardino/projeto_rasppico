const express = require('express');
const cors = require('cors');
const app = express();
const mongoose = require('mongoose');
const Sensor = require('./models/sensorModel');


app.use(express.json()); 
app.use(cors());

app.get('/receber', async (req, res) => {
    try {
        const sensors = await Sensor.find({});
        res.status(200).json(sensors);
    } catch (error) {
        res.status(500).json({message: error.message});
    }
}) // db.col.find().sort({"datetime": -1}).limit(1)

app.get('/receber_ultimo', async (req, res) => {
    try {
        const sensor_ultimo = await Sensor.find().sort({"id": -1}).limit(1)
        res.status(200).json(sensor_ultimo);
    } catch (error) {
        res.status(500).json({message: error.message});
    }
}) // find().sort({"datetime": -1}).limit(1)

app.get('/receber/:id', async (req, res) => {
    try {
        const {id} = req.params;
        const sensor = await Sensor.findById(id);
        res.status(200).json(sensor);
    } catch (error) {
        res.status(500).json({message: error.message});
    }
})


app.post('/enviar', async (req, res) => {
    try {
        const sensor = await Sensor.create(req.body);
        res.status(200).json(sensor);
    } catch (error) {
        console.log(error.message);
        res.status(500).json({message: error.message});
    }
  });


mongoose.set('strictQuery', false)

mongoose.connect('mongodb+srv://admin:root@motobmw.9krdce4.mongodb.net/Node-API?retryWrites=true&w=majority')
.then(() => {
    console.log('Conectado ao MongoDB.')
    app.listen(3000, '0.0.0.0', () => {
        console.log('Listening to port:  ' + 3000);
    });
}).catch((error) => {
    console.log(error);
})


// email: projetomotobmw@gmail.com
// senha: motobmwufsc

// mongoose: username: admin ; senha: root
// mongodb+srv://admin:<password>@motobmw.9krdce4.mongodb.net/?retryWrites=true&w=majority
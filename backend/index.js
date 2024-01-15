const express = require('express');
const cors = require('cors');
const app = express();
const mongoose = require('mongoose');
const { Sensor, sensorSchema }= require('./models/sensorModel');

app.use(express.json()); 
app.use(cors());

let SensorModel;

let ip;

app.get('/teste', async (req, res) => {
    try {
        res.status(200).json("teste");
    } catch (error) {
        res.status(500).json({message: error.message});
    }
})

app.post('/button_pressed', async (req, res) => {
    try { 
        const index_collection_name = 'sensor' + req.body['contador'];
        SensorModel = mongoose.model(index_collection_name, sensorSchema);
        res.status(200).json(req.body);
    } catch (error) {
        console.log(error.message);
        res.status(500).json({message: error.message});
    }
    });

app.get('/receber', async (req, res) => {
    try {
        const sensors = await SensorModel.find({});
        res.status(200).json(sensors);
    } catch (error) {
        res.status(500).json({message: error.message});
    }
})

app.get('/receber_ultimo', async (req, res) => {
    try {
        const sensor_ultimo = await SensorModel.find().sort({"id": -1}).limit(1)
        res.status(200).json(sensor_ultimo);
    } catch (error) {
        res.status(500).json({message: error.message});
    }
})

app.get('/receber/:id', async (req, res) => {
    try {
        const {id} = req.params;
        const sensor = await SensorModel.findById(id);
        res.status(200).json(sensor);
    } catch (error) {
        res.status(500).json({message: error.message});
    }
})


app.post('/enviar', async (req, res) => {
    try {
        create_sensor = await SensorModel.create(req.body);
        res.status(200).json(create_sensor);
    } catch (error) {
        console.log(error.message);
        res.status(500).json({message: error.message});
    }
  });

app.post('/enviar_hex', async (req, res) => {
try {
    console.log(req.body);
    res.status(200).json(req.body);
} catch (error) {
    console.log(error.message);
    res.status(500).json({message: error.message});
}
});

app.post('/ip', async (req, res) => {
    try {
        ip = req.body;
        res.status(200).json(req.body);
    } catch (error) {
        console.log(error.message);
        res.status(500).json({message: error.message});
    }
})

app.get('/ip', async (req, res) => {
    try {
        res.status(200).json(ip);
    } catch (error) {
        console.log(error.message);
        res.status(500).json({message: error.message});
    }
})




mongoose.set('strictQuery', false)

mongoose.connect('mongodb+srv://admin:root@motobmw.9krdce4.mongodb.net/Node-API?retryWrites=true&w=majority')
.then(() => {
    console.log('Conectado ao MongoDB.')
    app.listen(3001, '0.0.0.0', () => {
        console.log('Listening to port:  ' + 3001);
    });
    //const Teste = mongoose.model('testando', sensorSchema);
}).catch((error) => {
    console.log(error);
});


// email: projetomotobmw@gmail.com
// senha: motobmwufsc

// mongoose: username: admin ; senha: root
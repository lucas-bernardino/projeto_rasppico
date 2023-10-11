const express = require('express');
const cors = require('cors');
const app = express()

let dados = []; // usar mongoDB ?

app.use(express.json()); 
app.use(cors());

app.get('/receber', (req, res) => {
    res.json(dados);
    res.send(dados)
})


app.post('/enviar', (req, res) => {
    const dado = req.body;
    console.log(dado);
    dados[0] = dado;
    res.send("Dado adicionado com sucesso.");
  });

app.listen(3000, '0.0.0.0', () => {
    console.log('Listening to port:  ' + 3000);
});

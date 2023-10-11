const express = require('express');
const app = express()

let dados = [];

app.use(express.json()); // Add this line to parse JSON data in POST requests

app.get('/receber', (req, res) => {
    res.json(dados);
})


app.post('/enviar', (req, res) => {
    const dado = req.body;
    console.log(dado);
    dados.push(dado);
    res.send("Dado adicionado com sucesso.");
  });

app.listen(3000, '0.0.0.0', () => {
    console.log('Listening to port:  ' + 3000);
});

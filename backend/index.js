const express = require('express');
const app = express()

app.get('/', (req, res) => {
    res.send("HELLO WORLD FROM NODE.")
})


app.post('/enviar', (req, res) => {
    const newPost = {
      id: 4,
      title: req.body.title
    };
    res.json(newPost);
  });

app.listen(3000, '0.0.0.0', () => {
    console.log('Listening to port:  ' + 3000);
});

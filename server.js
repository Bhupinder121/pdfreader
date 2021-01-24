const express = require('express');
const fs = require('fs');

const app = express();

const {PythonShell} =require('python-shell');

 

var options = {
  mode: 'text',
  encoding: 'utf8',
  pythonOptions: ['-u'],
  scriptPath: './',
  pythonPath: 'D:\\Python\\python'
}


var file = fs.readdirSync('D:\\pdfreader\\templates\\audio');

const port =process.env.PORT || 3000;
const WebSocket= require('ws')
const wss = new WebSocket.Server({port:8080});


lines=[]
app.listen(port,()=>{console.log('listening...')})

app.use('/color',express.static('templates'));

var x =file[0]
var A = false


wss.on('connection',function(ws,req){
  console.log('connected');
  CheckWhatToSent()
  ws.send(x);
  file.shift()
  ws.on('message',function(data){
    if(data=="src"){
      CheckWhatToSent()
      x =file[0]
      ws.send(x);
      file.shift()
      
    }
    
  });
  ws.onclose = function(event){
    console.log('D')
  }
});

function CheckWhatToSent(){
  if (file.length==0){
    file = fs.readdirSync('D:\\pdfreader\\templates\\audio');
    x =file[0];
  }
  if (file.length==1){
    PythonShell.run('pdfReader.py',options,function(){
      
    })
  }
  
}
   
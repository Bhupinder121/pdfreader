$(document).ready(function() {
  var state = "paused";
  $('#pause').on('click', function() {
    if(state == 'paused') {
      state = "playing";
      $("#circle").attr("class", "play");
      $("#from_pause_to_play")[0].beginElement();
    } else {
      state = "paused";
      $("#circle").attr("class", "");
      $("#from_play_to_pause")[0].beginElement();
    }
  });
});

window.onload =function(){
  
  var socket = new WebSocket(`ws://:${process.env.PORT}`)

  var x = document.getElementById("myAudio");

  var Pbtn = document.getElementById('pause')

  var btn = $('.button')
  
  x.autoplay = false;
  var lines = [];

  socket.onmessage = function(event){
    x.setAttribute('src',"1.9audio\\"+event.data)
  }
  
  x.onended =function(){
    socket.send("src")
    socket.onmessage = function(event){
      x.setAttribute('src',"1.9audio\\"+event.data)
      x.autoplay = true;
      x.play();
    }
  }
  Pbtn.addEventListener('click',playPause)
  function playPause() { 
    if (x.paused) 
      x.play(); 
    else 
      x.pause(); 
  }

  
}
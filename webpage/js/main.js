let audioContext;
let scene;
let audioElement;
let audioElementSource;
let source;
let audioReady = false;

//Variables for room dimension and source/listener location
var widthR, heightR, depthR, widthS, heightS, depthS, widthL, heightL, depthL;


function validateForm(){
  
  var i, auxUp, auxDown, text, flag;
  let inputs = ["widthR", "heightR", "depthR", "widthS",
   "heightS", "depthS", "widthL", "heightL", "depthL"];

  for(i = 0; i < inputs.length; i++){
    var x = document.forms["myForm"][inputs[i]].value;
    
    if(i < 3){ auxUp = 25; auxDown = 0.5;}
    else{auxUp = 12.5; auxDown = -12.5;}


    if (x == "" || isNaN(x) || x <= auxDown || x >= auxUp) {
      text = "Input not valid";
      return text;      
    }
    else {
      sessionStorage.setItem(inputs[i], x);
      text = "Input OK";
    }

  }
  return text;
}


/**
 * @private
 */

function initAudio() {
  audioContext = new (window.AudioContext || window.webkitAudioContext);

  // Create a (1st-order Ambisonic) ResonanceAudio scene.
  scene = new ResonanceAudio(audioContext);

  // Send scene's rendered binaural output to stereo out.
  scene.output.connect(audioContext.destination);

  // Set room acoustics properties.
  let dimensions = {
    width: parseFloat(sessionStorage.getItem("widthR")),
    height: parseFloat(sessionStorage.getItem("heightR")),
    depth: parseFloat(sessionStorage.getItem("depthR")),
  };
  let materials = {
    left: 'brick-bare',
    right: 'curtain-heavy',
    front: 'marble',
    back: 'glass-thin',
    down: 'grass',
    up: 'transparent',
  };

  scene.setRoomProperties(dimensions, materials);

  // Create an audio element. Feed into audio graph.
  audioElement = document.createElement('audio');
  audioElement.src = 'http://recursostic.educacion.es/bancoimagenes/web/download.php?fileid=/bancoimagenes/contenidos/sonidos01/CD01/wav/amik00017.wav&aceptar=si';
  //https://file-examples-com.github.io/uploads/2017/11/file_example_WAV_1MG.wav
  audioElement.crossOrigin = 'anonymous';
  audioElement.load();
  audioElement.loop = true;

  audioElementSource = audioContext.createMediaElementSource(audioElement);

  // Create a Source, connect desired audio input to it.
  source = scene.createSource();
  audioElementSource.connect(source.input);

  // The source position is relative to the origin
  // (center of the room).
  source.setPosition(parseFloat(sessionStorage.getItem("widthS")),
    parseFloat(sessionStorage.getItem("heightS")), parseFloat(sessionStorage.getItem("depthS")));
  
  scene.setListenerPosition(parseFloat(sessionStorage.getItem("widthL")),
    parseFloat(sessionStorage.getItem("heightL")), parseFloat(sessionStorage.getItem("depthL")));

  audioReady = true;
}

let onLoad = function() {
  // Initialize play button functionality.
  let sourcePlayback = document.getElementById('playButton');
  sourcePlayback.onclick = function(event) {
    switch (event.target.textContent) {
      case 'Play': {
        if (!audioReady) {
          initAudio();
        }
        event.target.textContent = 'Pause';
        audioElement.play();
      }
      break;
      case 'Pause': {
        event.target.textContent = 'Play';
        audioElement.pause();
      }
      break;
    }
  };
  
  //Width --> y
  //Depth --> x


  if(parseFloat(sessionStorage.getItem("depthS")) !== 0){
    var sourceX = (parseFloat(sessionStorage.getItem("depthS")) + 
      parseFloat(sessionStorage.getItem("depthR"))) / 
      parseFloat(sessionStorage.getItem("depthS"));
  }else{sourceX = 0.5;}
  
  if(parseFloat(sessionStorage.getItem("widthS")) !== 0){
    var sourceY = (parseFloat(sessionStorage.getItem("widthS")) + 
      parseFloat(sessionStorage.getItem("widthR"))) / 
      parseFloat(sessionStorage.getItem("widthS"));
  }else{sourceY = 0.5;}


  if(parseFloat(sessionStorage.getItem("depthL")) !== 0){
    var listenerX = (parseFloat(sessionStorage.getItem("depthL")) / 
      parseFloat(sessionStorage.getItem("depthR"))) / 
      parseFloat(sessionStorage.getItem("depthL"));
  }else{listenerX = 0.5;}

  if(parseFloat(sessionStorage.getItem("widthL")) !== 0){
    var listenerY = (parseFloat(sessionStorage.getItem("widthL")) / 
      parseFloat(sessionStorage.getItem("widthR"))) / 
      parseFloat(sessionStorage.getItem("widthL"));
  }else{listenerY = 0.5;}

  let canvas = document.getElementById('canvas');
  let elements = [
    {
      icon: 'sourceIcon',
      x: sourceX,
      y: sourceY,
      radius: 0.04,
      alpha: 0.333,
      clickable: false,
    },
    {
      icon: 'listenerIcon',
      x: listenerX,
      y: listenerY,
      radius: 0.04,
      alpha: 0.616,
      clickable: false,
    },
  ];
  new CanvasControl(canvas, elements);
};
window.addEventListener('load', onLoad);

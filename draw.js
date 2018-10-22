var context = document.getElementsByTagName('canvas')[0].getContext("2d");
var canvas = document.getElementsByTagName('canvas')[0];

let model;

const modelURL = 'http://localhost:5000/tfjs_model/model.json';

const loadTsfModel = async (modelURL) => {
  if (!model) model = await tf.loadModel(modelURL);
}

loadTsfModel(modelURL)

var clickX = new Array();
var clickY = new Array();
var clickDrag = new Array();
var paint;

function resetCanvas(){
  clickX = new Array();
  clickY = new Array();
  clickDrag = new Array();
  paint;
}

canvas.addEventListener('mousedown', function(e){
  // resetCanvas();
  var mouseX = e.pageX - this.offsetLeft;
  var mouseY = e.pageY - this.offsetTop;

  paint = true;
  addClick(e.pageX - this.offsetLeft, e.pageY - this.offsetTop);
  redraw();
});

canvas.addEventListener('mousemove', function(e){
  if(paint){
    addClick(e.pageX - this.offsetLeft, e.pageY - this.offsetTop, true);
    redraw();
  }
});

canvas.addEventListener('mouseup', function(e){
  paint = false;
});


function addClick(x, y, dragging){
  clickX.push(x);
  clickY.push(y);
  clickDrag.push(dragging);
}

function redraw(){
  context.clearRect(0, 0, context.canvas.width, context.canvas.height); // Clears the canvas

  context.strokeStyle = "#000000";
  context.lineJoin = "round";
  context.lineWidth = 5;

  for(var i=0; i < clickX.length; i++) {
    context.beginPath();
    if(clickDrag[i] && i){
      context.moveTo(clickX[i-1], clickY[i-1]);
     }else{
       context.moveTo(clickX[i]-1, clickY[i]);
     }
     context.lineTo(clickX[i], clickY[i]);
     context.closePath();
     context.stroke();
  }
}

var button = document.getElementById('check-button');

button.onclick = function(){
  var doodle = canvas.toDataURL('image/png');

  var newImageTag = document.getElementsByClassName('imageToCheck')[0];
  newImageTag.src = doodle;

  predict(newImageTag);

  resetCanvas();
  context.clearRect(0, 0, canvas.width, canvas.height);
}


const predict = (newImage) => {
  // const newImage = document.getElementsByClassName('imageToCheck')[0];
  console.log(newImage)
  const processedImage = tf.fromPixels(newImage);
  const smallImg = tf.image.resizeBilinear(processedImage, [28, 28]);
  const resized = tf.cast(smallImg, 'float32');
  const prediction = model.predict(tf.reshape(resized, shape=[1, 28, 28, 3]));

  // const label = prediction.argMax().dataSync()[0];
  const label = prediction.dataSync()[0];
  console.log(label)
}
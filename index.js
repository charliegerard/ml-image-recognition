let model;

const modelURL = 'http://localhost:5000/tfjs_model/model.json';

const predict = async (modelURL) => {
  if (!model) model = await tf.loadModel(modelURL);

  const newImage = document.getElementsByClassName('image')[0];
  const processedImage = tf.fromPixels(newImage);
  const smallImg = tf.image.resizeBilinear(processedImage, [28, 28]);
  const resized = tf.cast(smallImg, 'float32');
  const prediction = model.predict(tf.reshape(resized, shape=[1, 28, 28, 3]));

  // const label = prediction.argMax().dataSync()[0];
  const label = prediction.dataSync()[0];
  console.log(label)

  // if(label === 0){
  //   console.log('circle')
  // } else if(label === 1){
  //   console.log('triangle')
  // }
}

predict(modelURL);




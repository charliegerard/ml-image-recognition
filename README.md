# Image classification using Keras and Tensorflow.js

### Install:

`pip install tensorflowjs`

`pip install numpy`

`pip install keras`

`pip install --upgrade pip`

`pip install --upgrade tensorflow`

`pip install --upgrade keras`

`pip install opencv-python`


```python
tensorflowjs_converter \
    --input_format=keras \
    model1.h5 \
    tfjs_model
```

### Adding new images in assets folder:

* Draw a doodle and save it as png
* Run the following python command to resize it to be compatible with google quickdraw dataset

```python
python resize.py <name of file>
```

* Add the newly resized files to the assets folder


### Getting assets from the quickdraw dataset:

* Open the convert.pde file in Processing.
* Change the name of the samples you want as well as the number.
* Download the right file from https://console.cloud.google.com/storage/browser/quickdraw_dataset/full/numpy_bitmap?pli=1
* Run the file


### Training the model:

```python
python cnn.py
```

### Predicting new images

At the moment i'm adding new images in the `new` folder:

```python
python predict.py
```

## To do:
* Import quickdraw dataset
* Add canvas prediction
- [x] Download some assets from the Google Quickdraw dataset

- [x] Convert .npy files from dataset to png

- [x] Add categories to prediction


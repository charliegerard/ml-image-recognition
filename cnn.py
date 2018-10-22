# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
import tensorflowjs as tfjs

classifier = Sequential()
classifier.add(Conv2D(32,(3,3), input_shape = (28,28,3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2,2)))
classifier.add(Flatten())
classifier.add(Dense(units = 128, activation="relu"))
classifier.add(Dense(units = 1, activation='sigmoid'))
classifier.compile(optimizer = 'adam', loss='binary_crossentropy', metrics=['accuracy'])

training_datagen = ImageDataGenerator(rescale = 1./255,
shear_range = 0.2,
zoom_range = 0.2,
horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale = 1./255)

training_set = training_datagen.flow_from_directory('assets/training_set',
target_size = (28,28),
batch_size = 20,
class_mode = 'binary')

test_set = test_datagen.flow_from_directory('assets/test_set',
target_size = (28,28),
batch_size = 4,
class_mode = 'binary')

classifier.fit_generator(training_set,
steps_per_epoch = 20,
epochs = 10,
validation_data = test_set,
validation_steps = 4)

# # serialize model to JSON
model_json = classifier.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
classifier.save_weights("model.h5")
classifier.save("model1.h5")

tfjs.converters.save_keras_model(classifier, "tfjs_model")

print("Saved model to disk")

print training_set.class_indices

# # -----------------

from keras.preprocessing import image

test_image = image.load_img('assets/new/circle/circle.png',
target_size = (28,28))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = classifier.predict(test_image)

print result

# #print training_set.class_indices

# if result[0][0] == 1:
#   prediction = 'triangle'
# else:
#   prediction = 'circle'

# print prediction

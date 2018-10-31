from keras.models import load_model
from keras.preprocessing import image
import numpy as np

model = load_model('model1.h5')
new_image = image.load_img('assets/new/bicycle/1.png', target_size=(28,28))
new_image = image.img_to_array(new_image)
new_image = np.expand_dims(new_image, axis = 0)
result = model.predict(new_image)

print result

# if result[0][0] == 0:
#   print "circle"
# else:
#   print "triangle"


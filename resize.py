import os, sys
from PIL import Image as img
import cv2

size = 28, 28

def crop(file):
  #Load the image in black and white (0 - b/w, 1 - color).
  img = cv2.imread(infile, 0)

  #Get the height and width of the image.
  h, w = img.shape[:2]

  #Invert the image to be white on black for compatibility with findContours function.
  imgray = 255 - img
  #Binarize the image and call it thresh.
  ret, thresh = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY)

  #Find all the contours in thresh. In your case the 3 and the additional strike
  _, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
  #Calculate bounding rectangles for each contour.
  rects = [cv2.boundingRect(cnt) for cnt in contours]

  #Calculate the combined bounding rectangle points.
  top_x = min([x for (x, y, w, h) in rects])
  top_y = min([y for (x, y, w, h) in rects])
  bottom_x = max([x+w for (x, y, w, h) in rects])
  bottom_y = max([y+h for (x, y, w, h) in rects])

  #Crop and save
  width = bottom_x - top_x
  height = bottom_y - top_y

  # Make sure the image cropped is a square
  if(width > height):
    difference = width - height
    crop_img = img[top_y:bottom_y+difference, top_x:bottom_x]
  elif (height > width):
    difference = height - width
    crop_img = img[top_y:bottom_y, top_x:bottom_x+difference]

  return crop_img

for infile in sys.argv[1:]:
  outfile = os.path.splitext(infile)[0]
  if infile != outfile:
    try:
      cropped_img = crop(infile)
      cv2.imwrite(outfile + ".png", cropped_img)

      resized_img = img.open(infile)
      resized_img.thumbnail(size, img.ANTIALIAS)
      resized_img.save(outfile + ".png")

    except IOError:
      print "cannot create thumbnail for '%s'" % infile

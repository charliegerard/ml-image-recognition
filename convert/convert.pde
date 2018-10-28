/*
Made by William Lehmus 2018
This tool converts NPY images to PNG format.

Based on the video tutorial by Daniel Schiffman. Link below.
https://www.youtube.com/watch?v=gX7U6WA7Ffk&index=2&list=PLRqwX-V7Uu6Zs14zKVuTuit6jApJgoYZQ
Get more data at: https://console.cloud.google.com/storage/browser/quickdraw_dataset/full/numpy_bitmap
This scetch converts .npy (numpy image format)
to png files and places in /data/ subdirectory
The google doodle images are 28x28 pixels = 784 pixels
Screen turns green when done.
*/

//--------------------------------------
//USER CHANGEABBLE PARAMETERS

int nr_of_images = 48;                                          //Number of images to extract from dataset
String output_folder = "cat";                                  //Name of subfolder to data to place images in /data/rainbow for instance
String dataset = sketchPath("cat.npy");        //Path to dataset file (.npy format)



//Load data from .npy files and print total size of data and nr of images
byte[] data = loadBytes(dataset);
println(data.length);                             //Size in bytes of the data
int total = (data.length -80) / 784;              //Number of images in dataset. .npy header size is 80 bytes. 28x28=784
println("Nr of images in data = " + total);

//Start extracting images
size(28,28);                                     //Screen size is 28x28 to allow save() function to save the image
int savefileindex = 0;                           //Index for naming files on export
byte[] outdata = new byte[nr_of_images*784];     //Prepare array
int outindex = 0;                                //Index
for (int n=0; n<nr_of_images; n++) {
 int start = 80 + n * 784;                       //.npy data format has 80 bytes of header data
 PImage img = createImage(28,28,RGB);            //Create empty image file
 img.loadPixels();                               //Load into 1d pixel array
  for (int i=0; i < 784; i++) {
    int index = i + start;                       //Starting pos for every new image in the 1d array
    byte val = data[index];                      //Extract image (784 bytes from array to new variable
    outdata[outindex] = val;                     //
    outindex++;
                                                 //images are signed bytes. - 255 to 255 value
    img.pixels[i] = color(255- val & 0xff);      //Bitwise operation to change from signed byte to unsigned byte. -255 to invert colors
  }

img.updatePixels();                              //Load bytes from 1d array to PImage object
  //int x = 28 * (n % 10);                         //Create rows. With some changes it can be used to show gallery of images
  //int y = 28 * (n / 10);                         //Create columns. With some changes it can be used to show gallery of images
  background(255);                                 //White out background before drawing on screen
  image(img,0,0);                                  //Draw image on screen
  //Save the drawn image to new png file
  save("data/" + output_folder + "/" + savefileindex + ".png");
  savefileindex++;                                 //Continue to next image
  println("Converting image " +savefileindex + " out of " + nr_of_images + " files");  //Print outs in console
}

println("Conversion done");
background(0,255,0);                              //Screen turns green when done converting

//saveBytes("rainbows.bin", outdata);    //save array of bytes in binary form

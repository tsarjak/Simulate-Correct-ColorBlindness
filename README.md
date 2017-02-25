# Simulate-Correct-ColorBlindness
This Script converts images to simulate Colour blindness using Daltonization Algorithm. The converted image is what is perceived by colour blind people. It also converts the image to help colour blind people differentiate between certain colours in an Image, using and HSV-Shifting Algorithm.

### Libraries Required:
PIL, colorsys, numpy
```shell
sudo pip install Pillow colorsys numpy
```
### To Install
```shell
git clone https://github.com/tsarjak/WallpapersFromReddit.git
```
### To run the code
In terminal:
```shell
#In Home Directory or the Directory in which you cloned/downloaded/installed the script

python transform.py -input <input file name> -output <output file name> -sp

python transform.py --help #For Help from terminal

#-sp to Simulate Protanopia
#-sd to Simulate Deutranopia
#-st to Simulate Tritanopia
#-correct to correct the image for protanopia patients
```

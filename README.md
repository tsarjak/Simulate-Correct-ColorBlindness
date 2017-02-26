# Simulate-Correct-ColorBlindness
This Script converts images to simulate Colour blindness using Daltonization Algorithm. The converted image is what is perceived by colour blind people. It also converts the image to help colour blind people differentiate between certain colours in an Image, using and HSV-Shifting Algorithm.

### Libraries Required:
PIL, colorsys, numpy
```shell
sudo pip install Pillow colorsys numpy
```
### To Install
```shell
git clone https://github.com/tsarjak/Simulate-Correct-ColorBlindness.git
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

### Examples

#### Simulating Protanopia

Original Image : ![plate15](https://cloud.githubusercontent.com/assets/9898343/23335798/0750036a-fbe3-11e6-9295-15ea03c8429c.jpg) 

Simulated Image: 
![plate15sim](https://cloud.githubusercontent.com/assets/9898343/23335813/5509b8b2-fbe3-11e6-8fd5-fc93016e7542.jpg) (How protanopes will percieve the image!) :

#### Correcting Protanopia

Original Image and How Protanopes will Perceive it : ![before_1](https://cloud.githubusercontent.com/assets/9898343/23335851/f23b4682-fbe3-11e6-9fea-2f313c6c6dd3.png)

Correcting the above original image and then Simulating it for Protanopes. The number which were unreadable for protanopes have now become clear enough to be recognised! : ![comb26022017053044](https://cloud.githubusercontent.com/assets/9898343/23335899/db0687f0-fbe4-11e6-9d92-f60bf15a5ff1.jpg)


_Currently Corrects only Protanopia Color Blindness via transformation. Deutranopia and Tritanopia to be added soon!_

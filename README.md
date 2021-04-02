# Simulate Colorblindness and Correct Colors for People with Colorblindness

This Script simulates images based on how people with colorblindness would perceive it naturally. You can also vary the degree of colorblindness for simulating. This script can also be used to correct images, making differenciation of certain colors in an image easier for people with colorblindness.

* **Easy** to setup and run!
* Simulate **Protanopia, Deutranopia, Tritanopia and Hybrid Colorblindess (Protanopia+Deutranopia).**
* **Correct colors** in images for **Protanopia, Deutranopia and Hybrid Colorblindness.**
* **Vary the degree of colorblindness** for both Simulation and Correction!
* Extremly **fast.**
* Use it from the **command line (super easy)**, or use it as a **library (advanced users).**
* Supports **Daltonization and HSV Shifting algorithm.**


## Installation

### Downloading the script

Go to the directory of your choice in terminal, and run the command below.
```shell
git clone https://github.com/tsarjak/Simulate-Correct-ColorBlindness.git
```

### Installing dependencies

To run this script, you need to install three libraries for python. Use pip or conda (or any package manager of your choice) to download PIL, Numpy and OpenCV.
```shell
sudo pip install Pillow numpy opencv-python
```

### Verifying the installation

Once you have successfully downloaded the scripts, and installed the dependencies, we can verify the installation.
The *~/Examples_Check/* folder contains a sample image containing a number of Ishihara plate images. 
We want to run the script on this example image and see if everything is working fine.

```shell
# Go to the directory where you downloaded the scripts.
cd <dir where scripts are downloaded>/Simulate-Correct-Colorblindness

# Now run the examples script.
python run_examples.py
```

This will run all the available algorithms on the example image, and save the processed images in the *Examples_Check/* directory.
Check the directory and see if you have 5 processed + 1 original image.


### Examples

#### Simulating Protanopia

Original Image : ![plate15](https://cloud.githubusercontent.com/assets/9898343/23335798/0750036a-fbe3-11e6-9295-15ea03c8429c.jpg) 

Simulated Image: 
![plate15sim](https://cloud.githubusercontent.com/assets/9898343/23335813/5509b8b2-fbe3-11e6-8fd5-fc93016e7542.jpg) (How protanopes will percieve the image!) :

#### Correcting Protanopia

Original Image and How Protanopes will Perceive it : ![before_1](https://cloud.githubusercontent.com/assets/9898343/23335851/f23b4682-fbe3-11e6-9fea-2f313c6c6dd3.png)

Correcting the above original image and then Simulating it for Protanopes. The number which were unreadable for protanopes have now become clear enough to be recognised! : ![comb26022017053044](https://cloud.githubusercontent.com/assets/9898343/23335899/db0687f0-fbe4-11e6-9d92-f60bf15a5ff1.jpg)


_Currently Corrects only Protanopia Color Blindness via transformation. Deutranopia and Tritanopia to be added soon!_

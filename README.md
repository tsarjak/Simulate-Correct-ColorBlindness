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
Check the directory and see if you have 5 processed + 1 original image. The processed (verified) and the original image are tagged in this readme file. If you want to verify further, have a look at the images in your computer and the images here.


## Running the script

*Control flags and description (For command line/terminal usage)*

| Flag &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;| Args type &nbsp; &nbsp; &nbsp; &nbsp;| Description | Default  | Needed? |
| --------|:---------:|:-------:|:---:|---:|
| -input       | *string* | Path to the input image to simulate/correct. | *None* | Yes |
| -output      | *string* | Directory where all simulated/corrected images will be stored.| *None* | Yes |
| -protanopia_degree | *float: [0,1]* | Degree of protanopia to simulate/correct. | *1.0* | No |
| -deutranopia_degree | *float: [0,1]* | Degree of deutranopia to simulate/correct. | *1.0* | No |
| -tritanopia_degree | *float: [0,1]* | Degree of tritanopia to simulate/correct. | *1.0* | No |
| -sim_protanopia |  *None*  |    Use this flag to simulate Protanopia. | *False* | No |
| -sim_deutranopia |  *None*  |    Use this flag to simulate deutranopia. | *False* | No |
| -sim_tritanopia |  *None*  |    Use this flag to simulate tritanopia. | *False* | No |
| -sim_hybrid |  *None*  |    Use this flag to simulate hybrid colorblindness. | *False* | No |
| -correct_colors |  *None*  |    Use this flag to correct colors for protanopia and deutranopia. | *False* | No |
| -run_all |  *None*  |    Use this flag to perform all operations (simulate + correct). | *False* | No |
  

### *How to run the script*

Go to the directory
```shell
cd ~/Simulate-Correct-ColorBlindness
```

Run the script with flags.
Let's say we want to simulate only tritanopia, and correct the image 
for protanopia and deutranopia. We run the below command.
```shell
python recolor.py
  -input /Users/example_user/pictures/sample.jpg
  -output /Users/example_user/pictures/sample_dir/
  -protanopia_degree 0.9
  -deutranopia_degree 0.6
  -tritanopia_degree 0.5 
  -sim_tritanopia
  -correct_colors
```
  
 If you want to run all the operations, you can also use the -all flag. 
 We will keep the degrees as default (1.0) this time to focus on -run_all flag.
 ```shell
 python recolor.py
  -input /Users/example_user/pictures/sample.jpg
  -output /Users/example_user/pictures/sample_dir/
  -run_all
```
  
If you want to run correction for only protanopia, 
you can set the deutranopia_degree value to 0. 
Essentially forcing the algorithm to not assume deutranopia.
```shell
 python recolor.py
   -input /Users/example_user/pictures/sample.jpg
   -output /Users/example_user/pictures/sample_dir/
   -deutranopia_degree 0
   -correct_colors
```


## Example Simulation Results: 

### Original Image:
![example_original](https://user-images.githubusercontent.com/9898343/113453323-c0fb2880-93d3-11eb-8c5f-1df504233313.jpg)

### Simulating Protanopia, Degree = 1.0:
![example_simulate_protanopia](https://user-images.githubusercontent.com/9898343/113453334-c6587300-93d3-11eb-8bc7-b14317aa84e2.png)

### Simulating Deutranopia, Degree = 1.0:
![example_simulate_deutranopia](https://user-images.githubusercontent.com/9898343/113453346-c9536380-93d3-11eb-99c3-08a6a3cfb7d6.png)

### Simulating Tritanopia, Degree = 1.0:
![example_simulate_tritanopia](https://user-images.githubusercontent.com/9898343/113453354-cd7f8100-93d3-11eb-8349-ad58e030cbf2.png)

### Simulating Hybrid ColorBlindness, Protanopia_degree = Deutranopia_degree = 0.5
![example_simulate_hybrid](https://user-images.githubusercontent.com/9898343/113453912-02d89e80-93d5-11eb-8a5b-575b92f99eb6.png)


## Example Correction Results:
Here, we will first correct the images, and then simulate the corrected image, to see if the difference is noticable.

### Protanopia

#### Correcting for Protanopia, Protanopia_degree = 0.9, Deutranopia_degree = 0.0
![ex_corrected_protanopia](https://user-images.githubusercontent.com/9898343/113454436-3831bc00-93d6-11eb-9f11-34167fdec3b5.png)

#### Simulating the corrected image for protanopia. Protanopia_degree = 0.9.
![ex_simulate_corrected_protanopia](https://user-images.githubusercontent.com/9898343/113454441-3bc54300-93d6-11eb-9761-5468fa2e70e2.png)

### Deutranopia

#### Correcting for Deutranopia, Deutranopia_degree = 0.9, Protanopia_degree = 0.0
![ex_corrected_deutranopia](https://user-images.githubusercontent.com/9898343/113454444-41228d80-93d6-11eb-999e-aff3e2434fc5.png)

#### Simulating the corrected image for Deutranopia. Deutranopia_degree = 0.9.
![ex_simulate_corrected_deutranopia](https://user-images.githubusercontent.com/9898343/113454461-45e74180-93d6-11eb-88b7-caed402e949c.png)



# Multiprocessing in Python
 A sample code for multiprocessing in Python

### Data
 4k x 4k .JP2 images - 100

### Objective
 To convert .jp2 images into .PNG format using multiprocessing and compare the performance

### Installation Notes:  
 Error: AttributeError: module 'PIL._imaging' has no attribute 'jpeg2k_decoder'
 ```bash
sudo apt-get install libjpeg-dev
```

### Results 
#### Linux
 Without multiprocessing - 300 seconds   
 With multiprocessing (8 processes) - 72 seconds

 #### Windows
 Without multiprocessing - 186 seconds   
 With multiprocessing (8 processes) - 41 seconds  

 **Not sure why Windows performed better. Still looking for answers**



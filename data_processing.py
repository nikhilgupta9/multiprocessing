import os
from PIL import Image
from tqdm import tqdm
import time


def main():
    INPUT_FOLDER = 'data/input'
    OUTPUT_FOLDER = 'data/output'

    #Saving all the input image names into one list
    images = os.listdir(INPUT_FOLDER)

    # Creating folders for image downloading
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)


    #Start time

    start = time.time()


    for image in tqdm(images):
        inPath = INPUT_FOLDER + '/' + image
        outPath = (OUTPUT_FOLDER + '/' + image).split('jp2')[0] + 'PNG'
        img = Image.open(inPath)
        img.save(outPath)
    end = time.time()
    print(end - start)

if __name__ == "__main__":
    main()

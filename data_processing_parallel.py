import multiprocessing
import os
from PIL import Image
from tqdm import tqdm
import time

def jp2ToPNG(proc_id, partition, path_to_input, path_to_output):
    """
    This function exports .jp2 images to PNG format and exports them to the output folder
    :param proc_id: process id for multiprocessing
    :param partition: list of images
    :param path_to_input: image folder path
    :param path_to_output: output folder path
    :return:
    """
    n = len(partition)
    i = 0
    for image in partition:
        inPath = path_to_input + '/' + image
        outPath = (path_to_output + '/' + image).split('jp2')[0] + 'PNG'
        img = Image.open(inPath)
        img.save(outPath)

def split(l, n_of_partitions):
    """
    Splits the given list l into n_of_partitions partitions of approximately equal size.
    :param l:
    :param n_of_partitions:
    :return: a list of the partitions (lists).
    """
    k, m = divmod(len(l), n_of_partitions)
    return [l[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n_of_partitions)]

def main():

    PROCESSES = 8
    INPUT_FOLDER = 'data/input'
    OUTPUT_FOLDER = 'data/output'

    # Creating folders for image downloading
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    #Saving all the input image names into one list
    images = os.listdir(INPUT_FOLDER)

    partitions = split(images, PROCESSES)
    proc_id = 1
    jobs = []

    #Start time
    start = time.time()

    for partition in partitions:
        process = multiprocessing.Process(target=jp2ToPNG,
                                          args=(proc_id, partition, INPUT_FOLDER, OUTPUT_FOLDER))
        jobs.append(process)
        proc_id = proc_id + 1

    for j in jobs:
        j.start()

    for j in jobs:
        j.join()

    end = time.time()
    print(end - start)

if __name__ == "__main__":
    main()


# Imports python modules
from os import listdir

# Extract pet labels from image filenames.
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames
    of the image files. These pet image labels are used to check the accuracy
    of the labels that are returned by the classifier function, since the
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Creates list of files in directory
    in_files = listdir(image_dir)

    # Creates empty dictionary for the results (pet labels, etc.)
    results_dic = dict()

    # Processes through each file in the directory, extracting only the words
    # of the file that contain the pet image label
    for idx in range(0, len(in_files), 1):

        # Skips file if starts with . (like .DS_Store of Mac OSX) because it
        # isn't a pet image file
        if in_files[idx][0] != ".":

            # Creates temporary label variable to hold pet label name extracted
            pet_label = ""

            # TODO 2a: Extract the pet label from the filename.
            # Lowercase the filename and split it into words on underscores
            word_list = in_files[idx].lower().split("_")

            # Keep only the words made entirely of letters, which drops the
            # number and file extension part (ex. '02259.jpg')
            for word in word_list:
                if word.isalpha():
                    pet_label += word + " "

            # Strip the trailing whitespace left by the loop
            pet_label = pet_label.strip()

            # If filename doesn't already exist in dictionary add it and its
            # pet label - otherwise print an error message because indicates
            # duplicate files (filenames)
            if in_files[idx] not in results_dic:
                results_dic[in_files[idx]] = [pet_label]

            else:
                print("** Warning: Duplicate files exist in directory:",
                      in_files[idx])

    # TODO 2b: Return the results_dic dictionary
    return results_dic

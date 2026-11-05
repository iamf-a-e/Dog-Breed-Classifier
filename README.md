# Dog Breed Classifier

A Python project that uses pre-trained convolutional neural networks (CNNs) to decide whether a pet image shows a dog, identify the dog's breed, and compare three model architectures on accuracy and runtime.

Built by Tariro Faith Munzwa as part of Udacity's AI Programming with Python Nanodegree.

## The problem

A city dog show needs to check that every registered pet is actually a dog. Each registration includes a photo, and the filename carries the pet's true label (for example `Boston_terrier_02259.jpg`). The program classifies each image with a pre-trained CNN and compares the result to the label.

## Objectives

1. Correctly identify which images are dogs (even if the breed is wrong) and which are not.
2. Correctly classify the breed of the dogs.
3. Find which architecture (ResNet, AlexNet or VGG) does best on objectives 1 and 2.
4. Weigh runtime against accuracy to see whether a faster model would be "good enough".

## How it works

1. **Command line arguments** (`get_input_args.py`): image folder, model architecture and the dog names file.
2. **Pet labels** (`get_pet_labels.py`): builds a label from each filename, lowercased, with the number and extension removed.
3. **Classification** (`classify_images.py`): runs each image through the chosen CNN and checks whether the pet label appears in the classifier label.
4. **Dog or not a dog** (`adjust_results4_isadog.py`): uses `dognames.txt` to flag whether the pet label and the classifier label are dogs.
5. **Statistics** (`calculates_results_stats.py`): counts and percentages for dogs, not-dogs and breeds.
6. **Printing** (`print_results.py`): summary, incorrect dog or not-dog calls, incorrect breeds.
7. **Timing** (`check_images.py`): total runtime in `hh:mm:ss`.

Results are stored in a dictionary of lists, one per image:
`[pet_label, classifier_label, match, pet_is_dog, classifier_is_dog]`

## Repository layout

```
check_images.py              main program
get_input_args.py
get_pet_labels.py
classify_images.py
adjust_results4_isadog.py
calculates_results_stats.py
print_results.py
classifier.py                provided by Udacity
dognames.txt
pet_images/                  40 images: 30 dogs and 10 not-dogs
uploaded_images/             extra images used to test the models
*_pet-images.txt             saved output for each architecture
*_uploaded-images.txt        saved output for the uploaded images
run_models_batch.sh          runs all three architectures
```

## Setup

Python 3 with PyTorch, torchvision and Pillow:

```
python3 -m venv venv
source venv/bin/activate
pip install pillow torch torchvision
```

The first run of each architecture downloads its pre-trained weights, so it needs an internet connection and takes longer.

## Usage

```
python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
python check_images.py --dir pet_images/ --arch alexnet --dogfile dognames.txt
python check_images.py --dir pet_images/ --arch resnet --dogfile dognames.txt
```

| Argument | Meaning | Default |
|---|---|---|
| `--dir` | Folder of images | `pet_images/` |
| `--arch` | `vgg`, `alexnet` or `resnet` | `vgg` |
| `--dogfile` | Text file of dog names | `dognames.txt` |

## Results

Measured on the 40 images in `pet_images/`.

| Metric | AlexNet | ResNet | VGG |
|---|---|---|---|
| Correctly classified dogs (%) | [value](#) | [value](#) | [value](#) |
| Correctly classified not-dogs (%) | [value](#) | [value](#) | [value](#) |
| Correctly classified breeds (%) | [value](#) | [value](#) | [value](#) |
| Overall label matches (%) | [value](#) | [value](#) | [value](#) |
| Runtime (hh:mm:ss) | [value](#) | [value](#) | [value](#) |

Full output for each run is in `alexnet_pet-images.txt`, `resnet_pet-images.txt` and `vgg_pet-images.txt`.

## Conclusion

[Which architecture performed best on dog versus not-dog detection and on breed accuracy, and how much longer it took than the others.](#)

[Whether the faster model would have been good enough, and why.](#)

## Observations

- Breeds that look alike are the main source of mistakes, for example Great Pyrenees and Kuvasz, German Shepherd and Malinois, and Beagle and Walker Hound.
- Dog or not-dog accuracy is higher than breed accuracy for every model, because the classifier can name a wrong breed and still correctly call the image a dog.
- [Anything notable from the images in `uploaded_images/`.](#)

## Notes

The classifier module and starter files were provided by Udacity. The functions listed above were written for this project.

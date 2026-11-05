
def adjust_results4_isadog(results_dic, dogfile):
    """
    Adds dog/non-dog flags to each image result.

    Dog names in dogfile may include comma-separated aliases. Each alias is
    treated as a valid dog label for both the pet and classifier labels.
    """
    with open(dogfile, "r") as infile:
        dog_names = {
            alias.strip().lower()
            for line in infile
            for alias in line.split(",")
            if alias.strip()
        }

    for result in results_dic.values():
        pet_label = result[0].strip().lower()
        classifier_labels = (
            alias.strip().lower() for alias in result[1].split(",")
        )
        pet_is_dog = int(pet_label in dog_names)
        classifier_is_dog = int(
            any(label in dog_names for label in classifier_labels)
        )
        result.extend((pet_is_dog, classifier_is_dog))

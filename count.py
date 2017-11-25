import numpy as np

test_total_count = 0
test_cat_count = np.zeros((11, ))
valid_total_count = 0
valid_cat_count = np.zeros((11, ))

categories = {'yes': 0,
              'no': 1,
              'up': 2,
              'down': 3,
              'left': 4,
              'right': 5,
              'on': 6,
              'off': 7,
              'stop': 8,
              'go': 9
              }


with open("train/testing_list.txt") as test_samples:
    for line in test_samples:
        test_total_count += 1
        line_split = line.split('/')
        if line_split[0] in categories.keys():
            test_cat_count[categories[line_split[0]]] += 1
        else:
            test_cat_count[10] += 1

with open("train/validation_list.txt") as valid_samples:
    for line in valid_samples:
        valid_total_count += 1
        line_split = line.split('/')
        if line_split[0] in categories.keys():
            valid_cat_count[categories[line_split[0]]] += 1
        else:
            valid_cat_count[10] += 1

print("Total test: {}".format(test_total_count))
print("Test category count:\n{}\n{}\n".format(categories.keys(), test_cat_count))
print("Total valid: {}".format(valid_total_count))
print("Valid category count:\n{}\n{}\n".format(categories.keys(), valid_cat_count))
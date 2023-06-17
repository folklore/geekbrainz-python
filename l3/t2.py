import random;

elements = []

for i in range(10):
    elements.append(random.randrange(10))

print(elements)

uniq_dupl_elements = []

for i in elements:
    if elements.count(i) > 1:
        if i not in uniq_dupl_elements:
            uniq_dupl_elements.append(i)

print(uniq_dupl_elements)

# [4, 9, 3, 1, 5, 1, 5, 9, 3, 2]
# [9, 3, 1, 5]

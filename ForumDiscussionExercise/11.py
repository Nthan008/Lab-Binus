numbers = [0, 1, 1, 1, 2, 3, 7, 7, 23]
histogram = {}
for i in numbers:
    histogram[i] = histogram.get(i, 0) + 1
print(histogram)
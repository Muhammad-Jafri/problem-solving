# zip is used to combine two iterables, stops at the shortest

fruits = ["apple", "banana", "kiwis"]
score = [30,20,50]
combined = list(zip(fruits, score))
print(combined)

for f, s in zip(fruits, score):
    print(f"fruit {f} has score {s}")

extracted_fruits, extracted_scores = zip(*combined)
print(extracted_fruits)
print(extracted_scores)


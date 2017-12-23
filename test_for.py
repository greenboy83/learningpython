for i in range(0, 51, 5):
    print(i, end=" ")
print("\n")
word = "index"
low = -len(word)
high = len(word)
print("low = " + str(low) + ", high = " + str(high))
for i in range(low, high):
    print("word[", i, "]=", word[i])

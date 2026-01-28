def pair_print(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            print(f"{arr[i]} - {arr[j]}")

pair_print(["artichoke", "broccoli", "carrot", "daikon"])

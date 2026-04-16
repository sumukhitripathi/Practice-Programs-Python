def largest_common_prefix(words):
    if not words:
        print("No words provided")
        return

    prefix = ""
    for i, char in enumerate(words[0]):
        if all(w[i] == char for w in words if len(w) > i):
            prefix += char
        else:
            break

    print("Words  :", words)
    print("Prefix :", prefix if prefix else "No common prefix")

largest_common_prefix(["flower", "flow", "flight"])
largest_common_prefix(["dog", "car", "race"])
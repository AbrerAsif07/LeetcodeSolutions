# Input: s = "tree"
# Output: "eert"


def frequencySort(s: str):
    result = ""
    map = {}

    for ch in s:
        map[ch] = map.get(ch, 0) + 1

    sorted_frequency = sorted(map.items(), key=lambda x: x[1], reverse=True)
    for ch, freq in sorted_frequency:
        result = result + (ch * freq)
    return result


print(frequencySort(s="tree"))

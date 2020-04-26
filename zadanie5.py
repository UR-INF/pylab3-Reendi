doc = input("Wpisz nazwe pliku:")
file = open(doc + ".txt")
histogram = {}
while True:
    char = file.read(1)
    if not char:
        break
    if (char in histogram):
        il = histogram.get(char)
        histogram[char] = il + 1
    else:
        histogram[char] = 1
file.close()
print(histogram)

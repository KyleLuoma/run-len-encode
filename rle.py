
def compress(w):
    a = w.split("1")
    a = a[0:len(a) - 1]
    c = ""
    for run in a:
        r_c = ""
        bin_run_len = len(str(bin(len(run))[2:]))
        if bin_run_len > 1:
            for i in range(1, bin_run_len):
                r_c = r_c + "1"
        r_c = r_c + "0" + str(bin(len(run))[2:])
        c = c + r_c   
    return c

def build_bitmap(run_list):
    out = ""
    for entry in run_list:
        for i in range(0, entry[1]):
            out = out + entry[0]
    return out

run_list = [
    ["100101", 3],
    ["0", 12],
    ["1", 4],
    ["0", 1]
]

print(build_bitmap(run_list))


find_smallest = [
    #build_bitmap([[build_bitmap([["1", 1],["0", 2**12 - 1]]), 2**13]]), #196586 #Evenly distributed
    #build_bitmap([[build_bitmap([["1", 1],["0", 2**13 - 1]]), 2**12 - 1],["0", 2**12 - 1],["1",1]]), #196588 #Evenly distributed with final run reversed with 1 at the end
    build_bitmap([[build_bitmap([["0", 2**13 - 1], ["1", 1]]), 2**12]]) #Biggest so far 106496 #Evenly distributed starting with 0s
    
    
    #build_bitmap([["001", 2**12], ["0", 2**25 - 2**14]]) #001001...s then trailing 0s

    #Best case:
    #build_bitmap([["1", 2**12], ["0", 2**25 - 2**12]])#, #Ones first then all zeros
]

#count 1s in resulting bitmap:
one_count = 0
for l in find_smallest[0]:
    if l == "1":
        one_count = one_count + 1
print("There are", str(one_count), "1 values in the bitmap.")

validate = [
    "01000001"
]

test_strings = [
    "000000000000000000000000000000000000000000000000000111",
    "111000000000000000000000000000000000000000000000000000",
    "000000000000000000001110000000000000000000000000000000",
    "000000000000010000000000000000010000000000000000000000"
]

mf_test = [
    "10101010101010101010101010101010",
    "11001100110011001100110011001100",
    "11100011100011100011100011100010",
    "11110000111100001111100001111001",
    "11111111111111110000000000000000"
]

for test_string in find_smallest:
    compressed_string = compress(test_string)

    #print(test_string)
    #print(compressed_string)
    print("Test string length:", len(test_string))
    print("Compressed string length:", len(compressed_string))

    text_file = open("compressed.txt", "w")
    n = text_file.write(compressed_string)
    text_file.close()





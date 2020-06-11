substrings = set()
my_str = 'abrakadabra'

for i in range(len(my_str)):
    # print(f'i={i}')
    for j in range(i, len(my_str)):
        # print(f'j={j}')
        curr_str = my_str[i:j+1]
        # print(curr_str)
        if curr_str not in substrings:
            substrings.add(curr_str)
substrings = substrings - {'', my_str}
print(len(substrings))
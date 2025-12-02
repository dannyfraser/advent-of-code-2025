import textwrap

#input = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""

with open("day-2-input.txt") as f:
    input = f.read()

def parse_input(ranges:str):
    return [tuple(map(int, i.split("-"))) for i in ranges.split(",")]


def extract_range_values(lower:int, upper:int):
    return [i for i in range(lower, upper + 1)]

def check_valid(i:int) -> bool:
    i_text = str(i)
    len_i = len(i_text)
    half_i = int(len_i/2)
    for pat_len in range(1, half_i + 1):
        # extract all of the patterns
        patterns = textwrap.wrap(i_text, pat_len)
        if len(set(patterns)) == 1:
            return False
    return True

total = 0
ranges = parse_input(input)
for r in ranges:
    range_values = extract_range_values(r[0], r[1])
    for v in range_values:
        if not check_valid(v):
            total += v
print(total)
    
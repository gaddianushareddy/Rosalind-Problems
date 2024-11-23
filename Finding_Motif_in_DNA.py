def find_substring_positions(s, t):
    """
    Find all positions where string t occurs as a substring in string s.
    Positions are 1-based.
    """
    positions = []
    start = 0

    while True:
        # Find the next occurrence of t in s starting from 'start'
        start = s.find(t, start)

        if start == -1:
            # No more occurrences found, break the loop
            break

        # Append the 1-based index of the found substring
        positions.append(start + 1)

        # Move start to the next position after the current match
        start += 1

    return positions


def parse_file(file_path):
    """
    Parse the input file to get strings s and t.
    """
    with open(file_path, 'r') as file:
        s = file.readline().strip()  # First line is string s
        t = file.readline().strip()  # Second line is string t
    return s, t


# Input file path
file_path = './input_files/rosalind_subs.txt'

# Parse the file to get strings s and t
s, t = parse_file(file_path)

# Find all positions of t as a substring of s
positions = find_substring_positions(s, t)

# Print the positions as a space-separated string
print(" ".join(map(str, positions)))

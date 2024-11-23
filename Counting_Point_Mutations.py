def hamming_distance(s, t):
    """
    Calculate the Hamming distance between two strings s and t.
    """
    if len(s) != len(t):
        raise ValueError("Strings must be of equal length")
    return sum(1 for a, b in zip(s, t) if a != b)

def parse_file(file_path):
    """
    Parse a file containing two DNA strings and return them.
    """
    with open(file_path, 'r') as file:
        lines = file.read().strip().split('\n')
        if len(lines) != 2:
            raise ValueError("The file must contain exactly two lines")
        return lines[0], lines[1]

# Input file
file_path = './input_files/rosalind_hamm.txt'

# Parse the file to get the DNA strings
s, t = parse_file(file_path)

# Calculate the Hamming distance
distance = hamming_distance(s, t)

# Print the result
print(distance)

# Function to compute the reverse complement of a DNA string
def reverse_complement(dna):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    # Reverse the string and replace each nucleotide with its complement
    reverse_comp = ''.join(complement[base] for base in reversed(dna))
    return reverse_comp

# Parse the DNA string from a file
with open('./input_files/rosalind_revc.txt', 'r') as infile:
    dna_string = infile.readline().strip()

# Compute the reverse complement
result = reverse_complement(dna_string)

# Print the result
print(result)

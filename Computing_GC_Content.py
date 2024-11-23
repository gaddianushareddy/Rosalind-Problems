def calculate_gc_content(dna_sequence):
    """Calculate the GC-content of a DNA sequence."""
    gc_count = dna_sequence.count('G') + dna_sequence.count('C')
    return (gc_count / len(dna_sequence)) * 100


def parse_fasta(file_path):
    """Parse a FASTA file and return a dictionary of ID: sequence pairs."""
    sequences = {}
    with open(file_path, 'r') as file:
        current_id = None
        current_sequence = []

        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if current_id:
                    sequences[current_id] = ''.join(current_sequence)
                current_id = line[1:]  # Remove '>'
                current_sequence = []
            else:
                current_sequence.append(line)

        # Add the last sequence to the dictionary
        if current_id:
            sequences[current_id] = ''.join(current_sequence)

    return sequences


def find_highest_gc_content(file_path):
    """Find the ID and GC-content of the sequence with the highest GC-content."""
    sequences = parse_fasta(file_path)
    max_gc_id = None
    max_gc_content = 0

    for seq_id, sequence in sequences.items():
        gc_content = calculate_gc_content(sequence)
        if gc_content > max_gc_content:
            max_gc_content = gc_content
            max_gc_id = seq_id

    return max_gc_id, max_gc_content


# Input file
file_path = './input_files/rosalind_gc.txt'

# Find the sequence with the highest GC-content
highest_gc_id, highest_gc_content = find_highest_gc_content(file_path)

# Print the result
print(highest_gc_id)
print(f"{highest_gc_content:.6f}")

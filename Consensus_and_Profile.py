from collections import defaultdict


def parse_fasta(file_path):
    """
    Parse a FASTA file and return a list of DNA strings.
    """
    dna_strings = []
    with open(file_path, 'r') as file:
        current_dna = ""
        for line in file:
            line = line.strip()
            if line.startswith(">"):  # Header line, skip it
                if current_dna:
                    dna_strings.append(current_dna)
                current_dna = ""
            else:
                current_dna += line
        if current_dna:
            dna_strings.append(current_dna)  # Add the last DNA string
    return dna_strings


def calculate_profile_matrix(dna_strings):
    """
    Calculate the profile matrix for a list of DNA strings.
    The profile matrix counts occurrences of 'A', 'C', 'G', 'T' at each position.
    """
    n = len(dna_strings[0])  # Length of each DNA string
    profile_matrix = {'A': [0] * n, 'C': [0] * n, 'G': [0] * n, 'T': [0] * n}

    for dna in dna_strings:
        for i, nucleotide in enumerate(dna):
            profile_matrix[nucleotide][i] += 1

    return profile_matrix


def calculate_consensus_string(profile_matrix, n):
    """
    Calculate the consensus string based on the profile matrix.
    For each position, the most frequent nucleotide is selected.
    """
    consensus = []
    for i in range(n):
        # Find the nucleotide with the maximum count at position i
        max_count = -1
        consensus_nucleotide = ""
        for nucleotide in "ACGT":
            if profile_matrix[nucleotide][i] > max_count:
                max_count = profile_matrix[nucleotide][i]
                consensus_nucleotide = nucleotide
        consensus.append(consensus_nucleotide)

    return ''.join(consensus)


def print_profile_matrix(profile_matrix):
    """
    Print the profile matrix in the required format.
    """
    for nucleotide in "ACGT":
        print(f"{nucleotide}: {' '.join(map(str, profile_matrix[nucleotide]))}")


def main():
    # Input file path
    file_path = './input_files/rosalind_cons.txt'  # Path to your FASTA file

    # Step 1: Parse the DNA strings from the FASTA file
    dna_strings = parse_fasta(file_path)

    # Step 2: Calculate the profile matrix
    profile_matrix = calculate_profile_matrix(dna_strings)

    # Step 3: Calculate the consensus string
    consensus_string = calculate_consensus_string(profile_matrix, len(dna_strings[0]))

    # Step 4: Print the consensus string and profile matrix
    print(consensus_string)
    print_profile_matrix(profile_matrix)


# Run the main function
main()

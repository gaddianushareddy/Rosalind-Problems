def translate_rna_to_protein(rna_sequence):
    """
    Translate an RNA string into a protein string based on the RNA codon table.
    """
    # RNA codon table as a dictionary
    codon_table = {
        "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
        "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
        "UAU": "Y", "UAC": "Y", "UAA": "Stop", "UAG": "Stop",
        "UGU": "C", "UGC": "C", "UGA": "Stop", "UGG": "W",
        "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
        "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
        "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
        "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
        "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
        "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
        "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
        "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
        "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
        "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
        "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
        "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    }

    protein_string = ""
    # Iterate through the RNA sequence in chunks of 3 (codons)
    for i in range(0, len(rna_sequence), 3):
        codon = rna_sequence[i:i+3]
        amino_acid = codon_table.get(codon, "")
        if amino_acid == "Stop":  # Stop translation if a stop codon is encountered
            break
        protein_string += amino_acid

    return protein_string


def parse_file(file_path):
    """
    Parse a file to extract the RNA sequence.
    """
    with open(file_path, 'r') as file:
        rna_sequence = file.read().strip()
    return rna_sequence


# Input file path
file_path = './input_files/rosalind_prot.txt'

# Parse the file to get the RNA sequence
rna_sequence = parse_file(file_path)

# Translate the RNA sequence into a protein string
protein_string = translate_rna_to_protein(rna_sequence)

# Print the resulting protein string
print(protein_string)

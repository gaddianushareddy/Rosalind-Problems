# Open the input file containing the DNA string
with open('./input_files/rosalind_rna.txt') as infile:
    # Read the DNA string from the file
    dna_string = infile.readline().strip()

    # Replace all occurrences of 'T' with 'U' to transcribe RNA
    rna_string = dna_string.replace('T', 'U')

    # Print the resulting RNA string
    print(rna_string)

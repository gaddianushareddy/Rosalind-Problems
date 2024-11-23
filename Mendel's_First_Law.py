def calculate_dominant_phenotype_probability(k, m, n):
    """
    Calculate the probability of producing an individual with a dominant phenotype.
    k: Number of homozygous dominant organisms
    m: Number of heterozygous organisms
    n: Number of homozygous recessive organisms
    """
    total = k + m + n  # Total population

    # Probabilities of each pair
    prob_kk = (k / total) * ((k - 1) / (total - 1))
    prob_km = (k / total) * (m / (total - 1)) + (m / total) * (k / (total - 1))
    prob_kn = (k / total) * (n / (total - 1)) + (n / total) * (k / (total - 1))
    prob_mm = (m / total) * ((m - 1) / (total - 1)) * 0.75  # 75% chance of dominant phenotype
    prob_mn = (m / total) * (n / (total - 1)) * 0.5 + (n / total) * (m / (total - 1)) * 0.5
    prob_nn = (n / total) * ((n - 1) / (total - 1)) * 0.0  # 0% chance of dominant phenotype

    # Total probability of producing a dominant phenotype
    dominant_probability = prob_kk + prob_km + prob_kn + prob_mm + prob_mn + prob_nn

    return dominant_probability


def parse_file(file_path):
    """
    Parse a file to extract values of k, m, and n.
    """
    with open(file_path, 'r') as file:
        line = file.readline().strip()
        k, m, n = map(int, line.split())
    return k, m, n


# Input file path
file_path = './input_files/rosalind_iprb.txt'

# Parse file to get the values of k, m, and n
k, m, n = parse_file(file_path)

# Calculate the probability of a dominant phenotype
probability = calculate_dominant_phenotype_probability(k, m, n)

# Print the result
print(f"{probability:.5f}")

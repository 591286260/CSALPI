import numpy as np
import pandas as pd
from Bio import SeqIO
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor

fasta_file = "./data/selected_equence.fasta"
sequences = []
for record in SeqIO.parse(fasta_file, "fasta"):
    sequences.append(str(record.seq))


lengths = [len(seq) for seq in sequences]


max_length = max(lengths)


def pad_sequence(seq):
    num_padding = max_length - len(seq)
    padded_seq = seq + "N" * num_padding
    return padded_seq

with ThreadPoolExecutor() as executor:

    matrix = np.zeros((len(sequences), len(sequences)))
    for i, j in tqdm(((i, j) for i in range(len(sequences)) for j in range(len(sequences)) if i <= j), total=len(sequences) * (len(sequences) + 1) // 2, desc="Calculating cosine similarity"):
        a = np.array([ord(c) for c in padded_sequences[i]])
        cosine_sim = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
        matrix[i][j] = cosine_sim
        matrix[j][i] = cosine_sim

df = pd.DataFrame(matrix, columns=[f"seq{i+1}" for i in range(len(sequences))])
df.to_csv("./data/cosine_Lncsim_matrix.csv", index=False)

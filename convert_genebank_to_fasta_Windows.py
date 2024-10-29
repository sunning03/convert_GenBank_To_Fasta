from Bio import SeqIO
import os

# Define input file path and output file path
input_file = input("Enter the path of the GenBank file: ")
output_file = input("Enter the path of the output FASTA file (optional): ")

# If output_file is not provided, use the same name as the input file with .fasta extension
if not output_file:
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    output_file = f"{base_name}.fasta"

# Parse the GenBank file and save it as a FASTA file
with open(output_file, "w") as fasta_file:
    for seq_record in SeqIO.parse(input_file, "genbank"):
        # Print sequence ID and length
        print(f"Sequence ID: {seq_record.id}")
        print(f"Sequence Length: {len(seq_record)}")
        
        # Write the species name and sequence to the FASTA file
        fasta_file.write(f">{seq_record.id} {seq_record.description}\n")
        fasta_file.write(f"{seq_record.seq}\n")

print(f"Sequences have been successfully saved to {output_file}")

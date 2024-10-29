from Bio import SeqIO
import sys
import os

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python convert_genbank_to_fasta.py <input_file> [output_file]")
        sys.exit(1)

    # Define input file path
    input_file = sys.argv[1]

    # Determine output file path
    if len(sys.argv) == 3:
        output_file = sys.argv[2]
    else:
        # Default output file path: same name as input file but with .fasta extension
        output_file = os.path.splitext(input_file)[0] + ".fasta"

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

if __name__ == "__main__":
    main()
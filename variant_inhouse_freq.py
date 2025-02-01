import os
import pandas as pd

def merge_vcf_files(output_file="merged_data.txt"):
    with open(output_file, "w") as outfile:
        for filename in os.listdir():
            if filename.endswith(".vcf"):
                with open(filename) as infile:
                    outfile.write(infile.read())

def process_vcf_data(input_file="merged_data.txt", output_file="processed_data.txt"):
    df = pd.read_csv(input_file, sep='\t', usecols=[0, 1, 3, 4, 9], header=None)
    df.to_csv(output_file, sep='\t', index=False, header=False)
    
    df = df.astype(str).apply(lambda x: '-'.join(x), axis=1)
    transformed_file = "transformed_data.txt"
    df.to_csv(transformed_file, index=False, header=False)
    
    df = pd.read_csv(transformed_file, sep='-', usecols=[0], header=None)
    target_file = "target_data.txt"
    df.to_csv(target_file, index=False, header=False)
    
    replacements = {
        "A-1": "A-hom", "A-0": "A-het",
        "C-1": "C-hom", "C-0": "C-het",
        "G-1": "G-hom", "G-0": "G-het",
        "T-1": "T-hom", "T-0": "T-het"
    }
    
    for old, new in replacements.items():
        df.replace(old, new, inplace=True)
    
    final_output_file = "final_data.txt"
    df.to_csv(final_output_file, index=False, header=False)

def filter_frequencies(input_file="frequency_data.txt", output_file="filtered_data.txt"):
    df = pd.read_csv(input_file, sep='\t', header=None)
    df_filtered = df[df[0] > 20]
    df_filtered.to_csv(output_file, sep='\t', index=False, header=False)

def main():
    merge_vcf_files()
    process_vcf_data()
    filter_frequencies()
    print("Pipeline completed successfully.")

if __name__ == "__main__":
    main()

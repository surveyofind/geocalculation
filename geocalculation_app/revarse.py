input_file = "change.csv"

# Output CSV file name
output_file = "revarse.csv"

# Read data from CSV file
with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    # Read all lines from the input file
    lines = infile.readlines()
    
    # Reverse the order of lines
    lines.reverse()

    # Write all lines to the output file
    outfile.writelines(lines)

print("Data has been successfully reordered, and written to", output_file)
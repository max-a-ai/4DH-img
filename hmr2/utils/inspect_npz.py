import numpy as np
import os

def inspect_npz(npz_file, output_dir='.'):
    # Load the .npz file
    data = np.load(npz_file)
    
    # Create a README file
    output_file = os.path.join(output_dir, "README_npz.md")
    with open(output_file, 'w') as f:
        f.write(f"# Report for {os.path.basename(npz_file)}\n\n")
        f.write(f"## Overview\n\n")
        f.write(f"This `.npz` file contains {len(data.files)} arrays:\n")
        
        for key in data.files:
            array = data[key]
            f.write(f"- **{key}**: shape = {array.shape}, dtype = {array.dtype}\n")

        f.write("\n## Sample Data\n\n")
        for key in data.files:
            array = data[key]
            f.write(f"### {key} (First 5 entries)\n")
            if array.ndim == 1:
                f.write(f"{array[:5]}\n\n")
            else:
                f.write(f"{array[:5]}\n\n")

    print(f"README.md created at {output_file}")

# Example usage
inspect_npz('/home/max/Documents/4dh-img/hmr2_evaluation_data/hmr2_evaluation_data/3dpw_test.npz', output_dir='/home/max/Documents/4dh-img/hmr2/utils')

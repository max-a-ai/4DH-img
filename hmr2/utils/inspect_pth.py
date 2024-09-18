import torch
import os
def inspect_pth(pth_file, output_dir='.'):
    # Load the .pth file (assuming it is a dict-like object)
    data = torch.load(pth_file, map_location='cpu')
    
    # Create a README file
    output_file = os.path.join(output_dir, "README_placeholder_pth.md")
    with open(output_file, 'w') as f:
        f.write(f"# Report for {os.path.basename(pth_file)}\n\n")
        f.write(f"## Overview\n\n")
        
        if isinstance(data, dict):
            f.write(f"This `.pth` file contains {len(data)} keys:\n\n")
            for key, value in data.items():
                f.write(f"- **{key}**: type = {type(value)}\n")
                
                if isinstance(value, dict):
                    f.write(f"  - Dictionary with {len(value)} keys\n")
                    # Display the first 5 keys and their value types
                    for subkey, subvalue in list(value.items())[:]:  # all keys
                        f.write(f"    - **{subkey}**: type = {type(subvalue)}\n")
                        
                        # Print a few value examples based on their type
                        if isinstance(subvalue, torch.Tensor):
                            f.write(f"      - Tensor shape: {subvalue.shape}, dtype = {subvalue.dtype}\n")
                            f.write(f"      - First 2 values: {subvalue.view(-1)[:2].tolist()}\n")
                        elif isinstance(subvalue, (int, float, str)):
                            f.write(f"      - Value: {subvalue}\n")
                        elif isinstance(subvalue, list) and len(subvalue) > 0:
                            f.write(f"      - First 2 values: {subvalue[:2]}\n")
                        else:
                            f.write(f"      - Content: {str(subvalue)[:100]}...\n")  # Shortened output for complex types
                        
                elif isinstance(value, torch.Tensor):
                    f.write(f"  - Tensor shape: {value.shape}, dtype = {value.dtype}\n")
                    f.write(f"  - First 5 values: {value.view(-1)[:5].tolist()}\n")
                    
                elif isinstance(value, (int, float, str)):
                    f.write(f"  - Value: {value}\n")
                
                # Limit output to the first key-level for brevity
                f.write("\n")
        
        else:
            f.write(f"The file contains a {type(data)} object.\n")

    print(f"README.md created at {output_file}")

# Example usage
path_file = '/home/max/nas_drive/publicdatasets/backbones/vitpose/vitpose-backbones/vitpose-l.pth'
output_dir = path_file.replace('.pth', '.md')
inspect_pth(path_file, output_dir='/home/max/Documents/4dh-img/hmr2/utils')
# inspect_pth('/home/max/nas_drive/publicdatasets/backbones/vitpose/vitpose-backbones/vitpose-h.pth', output_dir='/home/max/Documents/4dh-img/hmr2/utils')
# inspect_pth(path_file, output_dir)
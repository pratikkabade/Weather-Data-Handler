import os

# Create necessary directories
directories = ['bin/data', 'bin/helpers', 'data']

for directory in directories:
    os.makedirs(directory, exist_ok=True)

print('Successfully created the necessary folders.')
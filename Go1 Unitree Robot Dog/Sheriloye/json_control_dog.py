import os
import subprocess

# Folder path containing JSON files and Node.js scripts
folder_path = r'C:\Users\charl\Desktop\Unitree-Go1-NodeJS-ChatGPT'

# Iterate over each file in the folder
for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)
    
    # Determine if the file is a Node.js script for execution
    if file_name.endswith('.js'):
        # Optional: If your Node.js script expects a JSON file as an argument, specify the JSON file path here
        json_file_path = 'path_to_your_json_file.json'
        
        # Execute Node.js script
        # If your script does not take JSON as input, remove `json_file_path` from the command
        node_command = ['node', file_path, json_file_path]
        subprocess.run(node_command)

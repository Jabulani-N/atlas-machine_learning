#!/usr/bin/env python3

import os

answer_loop = __import__('2-qa').answer_loop
directory = 'data/ZendeskArticles/'
reference = ''
file_count_max = 10
file_count = 0

# Loop through all files in the specified directory
for filename in os.listdir(directory):
    # Check if the file has a .md extension
    file_count += 1
    if filename.endswith('.md') and file_count < file_count_max:
        # Construct the full file path
        file_path = os.path.join(directory, filename)
        # Open and read the file, then append its contents to the reference variable
        with open(file_path, 'r', encoding='utf-8') as file:
            # Add a newline for separation
            reference += file.read() + "\n"
with open('data/ZendeskArticles/PeerLearningDays.md') as f:
    reference += f.read()
answer_loop(reference)

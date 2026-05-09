import streamlit as st
import os
import hashlib
from collections import defaultdict
def get_file_hash(filepath, chunk_size=8192):
    """Calculates the SHA-256 hash of a file."""
    hasher = hashlib.sha256()
    try:
        with open(filepath, 'rb') as f:
            while chunk := f.read(chunk_size):
                hasher.update(chunk)
        return hasher.hexdigest()
    except (OSError, IOError) as e:
        return None
def find_duplicates(directory):
    """Finds duplicate files in the given directory and returns them grouped."""
    size_dict = defaultdict(list)
    for root, _, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            try:
                size = os.path.getsize(filepath)
                size_dict[size].append(filepath)
            except OSError:
                continue

    duplicate_groups = []
    for size, paths in size_dict.items():
        if len(paths) > 1:
            hash_dict = defaultdict(list)
            for path in paths:
                file_hash = get_file_hash(path)
                if file_hash:
                    hash_dict[file_hash].append(path)
            for hash_val, duplicate_paths in hash_dict.items():
                if len(duplicate_paths) > 1:
                    duplicate_groups.append({
                        'size': size,
                        'hash': hash_val,
                        'files': duplicate_paths
                    })
                    
    return duplicate_groups
st.set_page_config(page_title="Duplicate File Finder", layout="centered")
st.title("📁 Duplicate File Finder")
st.write("Enter a folder path on your computer. The app will scan it and identify exact duplicate files by comparing their sizes and SHA-256 hashes.")
folder_path = st.text_input("Enter local folder path (e.g., C:/Users/Name/Documents or /Users/Name/Documents):")
if st.button("Find Duplicates", type="primary"):
    if not folder_path:
        st.warning("Please enter a directory path.")
    elif not os.path.isdir(folder_path):
        st.error("The path provided is not a valid directory. Please check the path and try again.")
    else:
        with st.spinner(f"Scanning `{folder_path}` for duplicates. This might take a while depending on the folder size..."):
            duplicates = find_duplicates(folder_path)
            
        if not duplicates:
            st.success("Hooray! No duplicate files found in this directory.")
        else:
            st.warning(f"Found {len(duplicates)} group(s) of exact duplicate files.")
            for i, group in enumerate(duplicates):
                size_mb = group['size'] / (1024 * 1024)
                
                with st.expander(f"Duplicate Group {i+1} — Size: {size_mb:.2f} MB"):
                    st.caption(f"**Hash:** `{group['hash']}`")
                    for file_path in group['files']:
                        st.code(file_path, language="text")
                        #to run streamlit app, use: streamlit run "Duplicate file finder.py"
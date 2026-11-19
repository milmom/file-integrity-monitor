import hashlib
import os

def scan_folder(folder):
  file_to_hash = {}
  for root, dirs, files in os.walk(folder):
    for name in files:
      current_root = os.path.join(root, name)
      current_hash = hash_file(current_root)
      file_to_hash[current_root] = current hash
  return file_to_hash
      

def hash_file(path):
  with open(path, "rb") as f:
    file_bytes = f.read()
    file_hash = hashlib.sha256(file_bytes).hexdigest()
    return file_hash

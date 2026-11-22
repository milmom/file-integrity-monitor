import hashlib
import os

def scan_folder(folder):
  file_to_hash = {}
  for root, dirs, files in os.walk(folder):
    for name in files:
      current_root = os.path.join(root, name)
      current_hash = hash_file(current_root)
      file_to_hash[current_root] = current_hash
  return file_to_hash
      

def hash_file(path):
  with open(path, "rb") as f:
    file_bytes = f.read()
    file_hash = hashlib.sha256(file_bytes).hexdigest()
    return file_hash

def compare(old, new):
  status = {'changed': [], 'added': [], 'deleted': []}
  for path in new:
    if path in new and path in old and old[path] != new[path]:
      status('changed').append(path)
    
    if path in new and path not in old:
      status('added').append(path)

  for path in old:
    if path in old and path not in new:
      status('deleted').append(path)

  return status

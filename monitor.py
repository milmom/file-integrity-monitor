import hashlib


def hash_file(path):
  with open(path, "rb") as f:
    file_bytes = f.read()
    file_hash = hashlib.sha256(file_bytes).hexdigest()
    return file_hash

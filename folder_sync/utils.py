import os
import hashlib

def create_directory_if_not_exists(path, logger):
    if not os.path.exists(path):
        os.makedirs(path)
        logger.info(f'Created directory: {path}')

def compute_md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
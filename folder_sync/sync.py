import os
import shutil
import hashlib
import logging
from .utils import create_directory_if_not_exists, compute_md5


class FolderSync:
    def __init__(self, source, replica, log_file):
        self.source = source
        self.replica = replica
        self.log_file = log_file
        self.logger = self.setup_logger()

    def setup_logger(self):
        logger = logging.getLogger("FolderSync")
        logger.setLevel(logging.INFO)

        handler = logging.FileHandler(self.log_file)
        handler.setLevel(logging.INFO)

        formatter = logging.FileHandler(self.log_file)
        handler.setFormatter(formatter)

        logger.addHandler(handler)
        return logger
    
    def sync(self):
        self.logger.info("Starting synchronization...")
        self.sync_folders()
        self.logger.info("Synchronization complete.")

    def sync_folders(self):
        for root, dirs, files in os.walk(self.source):
            relative_path = os.path.relpath(root, self.source)
            replica_root = os.path.join(self.replica, relative_path)

            create_directory_if_not_exists(replica_root, self.logger)

            for file in files:
                source_file = os.path.join(root, file)
                replica_file = os.path.join(replica_root, file)

                if not os.path.exists(replica_file) or compute_md5(source_file) != compute_md5(replica_file):
                    shutil.copy2(source_file, replica_file)
                    self.logger.info(f'Copied/Updated file: {source_file} to {replica_file}')
        
        self.cleanup_replica()

    def cleanup_replica(self):
        for root, dirs, files in os.walk(self.replica):
            relative_path = os.path.relpath(root, self.replica)
            source_root = os.path.join(self.source, relative_path)

            for file in files:
                replica_file = os.path.join(root, file)
                source_file = os.path.join(source_root, file)

                if not os.path.exists(source_file):
                    os.remove(replica_file)
                    self.logger.info(f'Deleted file: {replica_file}')

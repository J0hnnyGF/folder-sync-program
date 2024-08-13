# Folder Sync Program

This program synchronizes a source folder with a replica folder. It copies files from the source to the replica if they are new or have been updated, and it removes files from the replica that no longer exist in the source.

## How to Use

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/J0hnnyGF/folder-sync-program.git
    ```
2. Navigate to the project directory:
    ```bash
    cd folder-sync-program
    ```

### Running the Program

To run the program, execute the `main.py` file::

```bash
python main.py "path_to_source_folder" "path_to_replica_folder" 60 "path_to_log_file.log"
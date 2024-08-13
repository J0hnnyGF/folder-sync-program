import argparse
from time import sleep
from folder_sync.sync import FolderSync

def parse_arguments():
    parser = argparse.ArgumentParser(description='Synchronize source and replica folders.')
    parser.add_argument('source', type=str, help='Path to the source folder')
    parser.add_argument('replica', type=str, help='Path to the replica folder')
    parser.add_argument('interval', type=int, help='Synchronization interval in seconds')
    parser.add_argument('log_file', type=str, help='Path to the log file')
    return parser.parse_args()

def main():
    args = parse_arguments()
    folder_sync = FolderSync(args.source, args.replica, args.log_file)

    try:
        while True:
            folder_sync.sync()
            sleep(args.interval)
    except KeyboardInterrupt:
        print("Synchronization stopped by user.")

if __name__ == "__main__":
    main()

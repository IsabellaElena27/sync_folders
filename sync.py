import os
import shutil
import time
import argparse

source_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'source_folder')
replica_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'replica_folder')
log_file = os.path.join(os.path.expanduser('~'), 'Desktop', 'log_file.txt')


def sync_folders(source_path, replica_path, log_file):
    """
        Synchronize files and directories between the source folder and the replica folder.

        Parameters:
            source_path (str): The path to the source folder.
            replica_path (str): The path to the replica folder.
            log_file (str): The path to the log file.

        Returns:
            None
        """
    if not os.path.exists(replica_path):
        os.makedirs(replica_path)
        with open(log_file, 'a') as log:
            log.write(f'Created directory: {replica_path}\n')
            print(f'Created directory: {replica_path}')

    with open(log_file, 'a') as log:
        for root_path, dirs, files in os.walk(replica_path):
            for file in files:
                replica_file = os.path.join(root_path, file)
                source_file = os.path.join(source_path, os.path.relpath(replica_file, replica_path))

                if not os.path.exists(source_file):
                    os.remove(replica_file)
                    log.write(f'Removed: {replica_file}\n')
                    print(f'Removed: {replica_file}')

        for root_path, dirs, files in os.walk(source_path):
            for file in files:
                source_file = os.path.join(root_path, file)
                replica_file = os.path.join(replica_path, os.path.relpath(source_file, source_path))

                if os.path.exists(replica_file) and os.path.getmtime(source_file) > os.path.getmtime(replica_file):
                    shutil.copy2(source_file, replica_file)
                    log.write(f'Updated: {replica_file}\n')
                    print(f'Updated: {replica_file}')

                elif not os.path.exists(replica_file):
                    shutil.copy2(source_file, replica_file)
                    log.write(f'Copied: {source_file} to {replica_file}\n')
                    print(f'Copied: {source_file} to {replica_file}')

            for dir in dirs:
                source_dir = os.path.join(root_path, dir)
                replica_dir = os.path.join(replica_path, os.path.relpath(source_dir, source_path))

                if not os.path.exists(replica_dir):
                    os.makedirs(replica_dir)
                    log.write(f'Created directory: {replica_dir}\n')
                    print(f'Created directory: {replica_dir}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("source_path")
    parser.add_argument("replica_path")
    parser.add_argument("log_file")
    parser.add_argument("sync_interval", type=int)

    args = parser.parse_args()

    while True:
        sync_folders(args.source_path, args.replica_path, args.log_file)
        time.sleep(args.sync_interval)

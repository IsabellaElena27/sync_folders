# sync_folders

The sync_folders() function syncronize files and directories between two folders, source folder and replica folder. 

# Steps:
1. Check if the replica folder exists, if not, the function creates it.
2. Sync files from replica to source
   - for each file in 'replica_folder', the function checks if it also exists in 'source_folder'; if the file doesn't exist in 'source_folder'(it was deleted), it is deleted from 'replica_folder'
3. Sync files from source to replica
   - for each file in 'source_folder', the function checks if it also exists in 'replica_folder';
   - if the file exists in 'replica_folder' and the version in 'source_folder' is updated, the file is copied from source to replica;
   - if the file doesn't exist in 'replica_folder', it is copied from source to replica;
4. Sync directories from source to replica
   - for each directory in 'source_folder', the function checks if it also exists in 'replica_folder'
   - if the directory doesn't exist, it is created

All the history of synchronization is logged in log_file and also printed in console.
The function runs in an infinite loop. It synchronize folders at a specified time interval.
It is created to be used on the command line. Paths to 'source_folder', 'replica_folder', 'log_file' and the sync interval are mandatory.

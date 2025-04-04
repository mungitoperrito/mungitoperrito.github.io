HOST="/mnt/e/FILES/"
DEST="/mnt/d/FILES/" 

rsync --stats \
       --recursive \
       --checksum \
       --delete-during \
       --delete \
       --no-perms \
       --progress \
       --itemize-changes \
       --log-file=rsync-log-files..$(date +'%Y-%m-%d')\
       ${HOST}${1}   ${DEST}

 
 #     --verbose \
 #     --dry-run \
 #
 #     ls > top-dirs   
 #     Remove windows sys files from top-dirs
 # USAGE:  for i in $(cat backup-files) ; do ./rsync-files.sh ${i} ; done

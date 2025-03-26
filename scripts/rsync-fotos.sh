HOST="/mnt/e/FOTOS/"
DEST="/mnt/d/FOTOS/" 

rsync --stats \
       --recursive \
       --checksum \
       --delete-during \
       --delete \
       --no-perms \
       --progress \
       --itemize-changes \
       --log-file=rsync-log-fotos..$(date +'%Y-%m-%d')\
       ${HOST}${1}   ${DEST}

 
 #     --verbose \
 #     --dry-run \
 #
 #     ls > top-dirs   
 #     Remove windows sys files from top-dirs
 # USAGE:  for i in $(cat backup-fotos) ; do ./rsync-fotos.sh ${i} ; done

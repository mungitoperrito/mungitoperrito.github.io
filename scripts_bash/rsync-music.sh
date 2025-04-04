MUSIC_DIR=/mnt/e/MUSIC/
BACKUP_DIR=/mnt/d/MUSIC/
DIR_LIST=$(ls ${MUSIC_DIR} |grep -v 'System ' | grep -v CYCLE)

 echo ${DIR_LIST} 

 for d in ${DIR_LIST} ; do 
    rsync --verbose \
          --recursive \
          --checksum \
          --delete-during \
          --delete \
          --force \
          --no-perms \
          --progress \
          --itemize-changes \
          --log-file=rsync-log-music..$(date +'%Y-%m-%d') \
          ${MUSIC_DIR}${d}   ${BACKUP_DIR}
 done

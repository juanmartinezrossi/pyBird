#!/bin/bash
#
# Sync local directory to remote directory.
#
# Modified by: Leo Mao
# Modified from: https://gist.github.com/evgenius/6019316
#
# Requires Linux, bash, inotifywait and rsync.
#
# To avoid executing the command multiple times when a sequence of
# events happen, the script waits one second after the change - if
# more changes happen, the timeout is extended by a second again.
#
# Example usage:
#
#    sh watchsync.sh
#
# Released to Public Domain. Use it as you like.

RASPI_IP= "10.42.0.1"
RASPI_PASS= "ubuntu"
SYNC_PERIOD_IN_SECONDS=5

RSYNC_OPTIONS="-Cait"
RSYNC_EXCLUDES="--exclude venv --exclude *.json --exclude .idea --exclude .git --exclude .gitignore --exclude watchsync.sh --exclude storage/* --exclude storage/*/*"
REMOTE_DIR="pdd@"$RASPI_IP":/home/pdd/deployment/pyBird/"
LOCAL_DIR="."

run() {
  echo "synching...";
  #sshpass -p $RASPI_PASS rsync $RSYNC_OPTIONS $RSYNC_EXCLUDES $LOCAL_DIR $REMOTE_DIR
  sshpass -p $RASPI_PASS rsync $LOCAL_DIR $REMOTE_DIR
  echo "synchronized.";
}

while true; do
  run
  sleep $SYNC_PERIOD_IN_SECONDS
  done

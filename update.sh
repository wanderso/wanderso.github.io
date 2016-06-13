#!/bin/bash

COMMITMSG="Default commit from update script"

for i in "$@"
do     
case $1 in
        -c | --commitmsg )      shift
                                COMMITMSG=$1
                                ;;
esac
done

git add --all
git commit -m "$COMMITMSG"
git push -u origin master

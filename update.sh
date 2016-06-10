#!/bin/bash

COMMITMSG="Ran default update script"

for i in "$@"
do
case $i in
    -c=*|--commitmsg=*)
    COMMITMSG="${i#*=}"
    shift # past argument=value
    ;;
esac
done

git add --all
git commit -m "$COMMITMSG"
git push -u origin master

#!/bin/bash


if (git cat-file -e 8c74235) ; then
  echo 'Commit exist'
  exit 0
else
  echo 'Commit does not exist'
  exit 1
fi

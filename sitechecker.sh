#!/bin/sh

PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/alves/code/lighthouse-desafio-2-eduardo-alves

full_path=$(realpath $0)
parent_dir=$(dirname $full_path)
cd $parent_dir

if test $# -eq 0
then
	echo "Running $0 with default arguments"
	python3 -m sitechecker -f ./input/urls.csv

else
	echo "Running $0 with $# arguments"
	echo "$@"
	python3 -m sitechecker $@
fi

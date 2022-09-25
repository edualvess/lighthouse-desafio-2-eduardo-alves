#!/usr/bin/env bash

if test $# -eq 0
then
	echo "Running $0 with default arguments"
	python3 -m sitechecker -f ./input/urls.csv

else
	echo "Running $0 with $# arguments"
	echo "$@"
	python3 -m sitechecker $@
fi

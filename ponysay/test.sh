#!/bin/bash

# Tests the various requirements for a working install
function test_installed()
{
	if ! [ -x "$(command -v $1)" ]; then
		echo "$1 is required but not installed or available."
		exit 1
	fi

	return 0
}

function test_directory()
{
	if ! [ -d "$1" ]; then
		echo "ponysay found, but ponies directory is non-standard. Check the value of $2 to make sure it points to the right spot!"
		return 1
	fi

	return 0
}

test_installed ls
test_installed php
test_installed sed
test_installed fortune
test_installed ansi2html
test_installed ponysay
test_installed ponythink

test_directory /usr/share/ponysay/ponies "$path_to_pony_files"

echo "Should run."

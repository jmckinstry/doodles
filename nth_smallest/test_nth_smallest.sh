#!/bin/bash

run_test() {
        input=$1
        #echo "Running '${input}':"
        #echo "python perfect.py ${input}"
        python nth_smallest.py ${input}
        echo ""
}

run_test
run_test 1\ 1\ 2\ 3\ 4\ 5\ 6\ 7\ 8\ 9\ 10
run_test 3\ 1\ 2\ 3\ 4\ 5\ 6\ 7\ 8\ 9\ 10

run_test 1\ 10\ 9\ 8\ 7\ 6\ 5\ 4\ 3\ 2\ 1
run_test 3\ 10\ 9\ 8\ 7\ 6\ 5\ 4\ 3\ 2\ 1

run_test 5\ 1\ 10\ 1000\ 10000\ 100000\ 1000000\ 10000000

#!/bin/bash

run_test() {
        input=$1
        #echo "Running '${input}':"
        #echo "python perfect.py ${input}"
        python perfect.py ${input}
        echo ""
}

run_test
run_test perfect\ makes\ practice
run_test a\ b\ c\ d
run_test a\ bb\ ccc\ dddd
run_test aaaa\ bbb\ cc\ d
run_test a
run_test a\ b\ serial\ d\ e
run_test a1\ b2\ c3\ d4\ e5
run_test All\ work\ and\ no\ p1ay\ makes\ such\ and\ such

#!/usr/bin/env sh

set -e

if ! command -v cmake &> /dev/null
then
    echo >&2 "You need to have CMake installed."
    exit
fi

if ! command -v mpiexec &> /dev/null
then
    echo >&2 "You need to have a MPI library installed (OpenMPI, MPICH etc.)."
    exit
fi

currdir=`pwd`

[ -d build ] || mkdir build
cd build
cmake -DCMAKE_RULE_MESSAGES=OFF  .. > /dev/null
make > /dev/null
mpiexec ./ppcd-6
cd $currdir

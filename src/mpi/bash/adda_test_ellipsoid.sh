#!/bin/bash
cd ..
for (( counter=1000; counter>0; counter-- ))
do

echo -n "ellipsoid: $counter "
b_a=0.$(( ($RANDOM%100)))
c_a=0.$(( ($RANDOM%100) ))
alpha=$(( ($RANDOM%360)))
beta=$(( ($RANDOM%360)))
gamma=$(( ($RANDOM%360)))
mpiexec -n 2 ./adda_mpi -shape ellipsoid $b_a $c_a -eq_rad 5 -orient $alpha $beta $gamma
done
printf "\n"


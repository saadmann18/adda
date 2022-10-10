#!/bin/bash
cd ..
for (( counter=1000; counter>0; counter-- ))
do

echo  "Box: $counter "

alpha=$(( ($RANDOM%360)))
beta=$(( ($RANDOM%360)))
gamma=$(( ($RANDOM%360)))

w=$((RANDOM%3+1))
h=$((RANDOM%3+1))

if [[ $w != $h ]]; then
mpiexec -n 2 ./adda_mpi -shape box $w $h -eq_rad 5 -orient $alpha $beta $gamma
fi
done
printf "\n"

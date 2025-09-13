#!/bin/bash

num=42
num1=1337
arr=("arr1" "arr2" "arr3")
declare -A arr_2

for var in ${arr[@]};do
    echo $var
done

if [$num -gt 10 ] ; then
    echo "ah"
else
    echo "la"
fi
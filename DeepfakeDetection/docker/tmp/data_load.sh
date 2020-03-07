#!/bin/bash
id=`printf %02d 0`

for i in ` seq 1 50`
do 
  num=`printf %02d $id`
  path="https://www.kaggle.com/c/16880/datadownload/dfdc_train_part_${num}.zip"
  wget --load-cookie cookies.txt $path
  id=$((id+1))
done
#!/bin/sh

awk 'BEGIN { FS=","; OFS=",";}
NR >= 2 { 
    print $4, $8, $9, $10, $11, $12, $13, $14, $15, $16, $17, $18, $19, $20, $21, $6, $8, $22, $23, $24, $25, $26, $27, $28, $29, $30, $31, $32, $33, $34;
    print $6, $8, $22, $23, $24, $25, $26, $27, $28, $29, $30, $31, $32, $33, $34, $4, $8, $9, $10, $11, $12, $13, $14, $15, $16, $17, $18, $19, $20, $21;
}' $1 $2 >| trainingMatrix.csv

# NR is 3 instead of 2 because we throw one line out
awk 'BEGIN { FS=","; OFS=",";}
NR >= 3 {
    print 1;
    print 0;
}' $1 $2 >| trainingVector.csv

sed -i.bak '/[a-z]/d' trainingMatrix.csv

rm -rf trainingMatrix.csv.bak



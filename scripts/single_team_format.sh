#!/bin/sh

awk 'BEGIN { FS=","; OFS=","; print "ID", "SCORE", "OT", "FGM", "FGA", "FGM3", "FGA3", "FRM", "FRA", "OR", "DR", "AST", "TO", "STL", "BLW", "PF";}
NR >= 2 { 
    winner=$1$3;
    loser=$1$5;
    print winner, $4, $8, $9, $10, $11, $12, $13, $14, $15, $16, $17, $18, $19, $20, $21;
    print loser, $6, $8, $22, $23, $24, $25, $26, $27, $28, $29, $30, $31, $32, $33, $34;
}' $1 $2 >| singleTeamGames.csv

sed -i.bak '/[a-z]/d' singleTeamGames.csv

rm -rf singleTeamGames.csv.bak

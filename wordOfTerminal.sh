#!/bin/bash

numLines=$(awk 'END{print NR}' /home/moly/Documents/Terminal/wordOfTerminal/paraulasCatala.txt)
bashLine=$(((RANDOM% numLines)+1))
bashDef=$(awk -v var=$bashLine 'FNR == var {print $0}' /home/moly/Documents/Terminal/wordOfTerminal/paraulasCatala.txt)
echo $bashDef

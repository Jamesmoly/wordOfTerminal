#!/bin/bash

numLines=$(awk 'END{print NR}' ~/Documents/Terminal/wordOfTerminal/definitions.txt)
bashLine=$(((RANDOM% numLines)+1))
bashDef=$(awk -v var=$bashLine 'FNR == var {print $0}' ~/Documents/Terminal/wordOfTerminal/definitions.txt)
echo $bashDef

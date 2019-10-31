#!/usr/bin/env bash
#
# Author:        Willian Ferreira
# Maintenance:   Willian Ferreira
#
# ------------------------------------------------------------------------ #
#  Script used to add e-mails on blacklist Cisco IronPort C380. 
#
# ------------------------------------------------------------------------ #
# Changelog:c
#
# v1.1.0 30/10/2019 - Willian Ferreira
#
# -------------------------------BASIC VARIABLES----------------------------------------- #

#Variables
SERVER = "IP/HOSTNAME"
DOM = "$(echo $1)"
VAL=""
SUSPECT= "blacklist"
DATA=`date '+%Y-%m-%d %H:%M:%S'`

# ------------------------------------------------------------------------ #

# -------------------------------FUNCTIONS----------------------------------------- #

validadeEmail(){

	ssh user@$SERVER "dictionaryconfig print $SUSPECT" >> suspeito.txt 

	if [ $? -eq 1 ];
	then
		echo "Sender or domain query in list error"
	else

		sed -i 's/"//g;s/.$//' suspect.txt  
		tr -d "," < suspect.txt > result.txt
		
		rm -rf suspect.txt

		cat result.txt | grep $DOM >> suspect.txt
		VAL="$(cat suspect.txt)"

		if [ "$VAL" = "" ];
		then
			blockEmail
		elif [ $VAL = $DOM ];
		then
			echo "$DOM domain already registered in Suspect list"
		else
			blockEmail
		fi
		rm -rf suspect.txt result.txt
	fi
}

blockEmail(){

	ssh user@$SERVER "dictionaryconfig edit $SUSPECT new $DOM; commit -y"

	if [ $? -eq 0 ];
	then
		echo "$DOM domain added to Suspect list"
	else 
		echo "Error adding domain $DOM to Suspect list."
	fi
}

main(){

	validadeEmail
}

# ------------------------------------------------------------------------ #

# -------------------------------EXECUTION----------------------------------------- #

main

# ------------------------------------------------------------------------ #

# imports
import hashlib
import os
from hash_func import hashing,deHashUPH
from colorama import Fore
# variables
banner = """
###################################################################################
\t\t\tKripto dastur\t\tauthor @knigga
###################################################################################
\n\n
\t_[1]__ Hash kodlash\t-
\t\t\t\t\tsha1//sha224//sha256//sha512//md5
\n\t_[2]__ Dehash\t-
\n
\t_[3]__ Chiqish\t\t-
#############################__________________####################################
"""
cmd = os.system

#functions
def menu():
	cmd("cls")
	main()

def choose_inside():
	in_choose = input(f"{Fore.GREEN}--------<[*]Bosh menuga qaytasizmi [1-ha 2-yo'q]\t>{Fore.WHITE}")
	if in_choose == '1':
		menu()


def main():
	cmd("cls")
	print(Fore.RED,banner,Fore.WHITE)
	choose = input(f"{Fore.GREEN}--------<[*]Tanlang > {Fore.WHITE}")
	if choose == '1':
		hashing()
		choose_inside()
	elif choose == '2':
		deHashUPH()
		choose_inside()
	else:
		exit()
if __name__ == '__main__':
	main()


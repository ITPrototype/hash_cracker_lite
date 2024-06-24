import hashlib
import os
from ggenerator import generator
from colorama import Fore
cmd = os.system
def hashing():
	cmd("cls")
	hash_value = input("--------<[*]So'zni kiriting\t\t\t>")
	print("Hash turlari: [MD5] [SHA1] [SHA256] [SHA224] [SHA512] ")
	hash_type = input("--------<[*]Hash turini tanlang\t\t\t>").lower()
	hashUPH(hash_type,hash_value)

def hashUPH(hashtype,hash_value):
	hash_t = None
	if hashtype == 'sha1':
		hash_t = hashlib.sha1()
	elif hashtype == 'sha224':
		hash_t = hashlib.sha224()
	elif hashtype == 'sha256':
		hash_t = hashlib.sha256()
	elif hashtype == 'sha512':
		hash_t = hashlib.sha512()
	elif hashtype == 'md5':
		hash_t = hashlib.md5()
	else:
		print("Unknown hash type")
	if hash_t:
		hash_t.update(hash_value.encode())
		hashed = hash_t.hexdigest()
		print(f"{hashtype.upper()}=>\t{hashed}")

def hashUPHret(hashtype,hash_value):
	hash_t = None
	if hashtype == 'sha1':
		hash_t = hashlib.sha1()
	elif hashtype == 'sha224':
		hash_t = hashlib.sha224()
	elif hashtype == 'sha256':
		hash_t = hashlib.sha256()
	elif hashtype == 'sha512':
		hash_t = hashlib.sha512()
	elif hashtype == 'md5':
		hash_t = hashlib.md5()
	else:
		print("Unknown hash type")
	if hash_t:
		hash_t.update(hash_value.encode())
		hashed = hash_t.hexdigest()
		return hashed

def deHashUPH():
	hash_code = input("--------<[*]Hash kod\t\t\t>")
	generator()
	with open("wlist.txt") as f:
		while True:
			line = f.readline().strip()
			if not line:
				break
			if hashUPHret('sha1',line) == hash_code:
				print(f'{Fore.BLUE}[!]FOUND =>\t\tHashtype:sha1\tWord:{line}')
				break
			elif hashUPHret('sha224',line) == hash_code:
				print(f'{Fore.BLUE}[!]FOUND =>\t\tHashtype:sha224\tWord:{line}')
				break
			elif hashUPHret('sha256',line) == hash_code:
				print(f'{Fore.BLUE}[!]FOUND =>\t\tHashtype:sha256\tWord:{line}')
				break
			elif hashUPHret('sha512',line) == hash_code:
				print(f'{Fore.BLUE}[!]FOUND =>\t\tHashtype:sha512\tWord:{line}')
				break
			elif hashUPHret('md5',line) == hash_code:
				print(f'{Fore.BLUE}[!]FOUND =>\t\tHashtype:md5\t{Fore.YELLOW}Word:{line}')
				break
		else:
			print(f'{Fore.RED}[x]NOT FOUND :(')

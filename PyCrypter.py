import os
import base64
from sys import argv
import colorama
from colorama import Fore

crypter_offset = 10
crypter_mark = '__PYCRYPTER_HA' * 100

def pycrypt(content):
    b64_content = base64.b64encode(content.encode()).decode()
    index = 0
    code = f'{crypter_mark} = ""\n'

    for _ in range(int(len(b64_content) / crypter_offset) + 1):
        _str = ''
        for char in b64_content[index:index + crypter_offset]:
            byte = str(hex(ord(char)))[2:]
            if len(byte) < 2:
                byte = '0' + byte
            _str += '\\x' + str(byte)
        code += f'{crypter_mark} += "{_str}"\n'
        index += crypter_offset
    code += f'exec(__import__("\\x62\\x61\\x73\\x65\\x36\\x34").b64decode({crypter_mark}.encode("\\x75\\x74\\x66\\x2d\\x38")).decode("\\x75\\x74\\x66\\x2d\\x38"))'

    return code

def pycrypt_startup():
    print(f"""
                                   {Fore.BLUE}w              
{Fore.RED}88b.{Fore.RESET} {Fore.MAGENTA}Yb  dP{Fore.RESET} {Fore.BLUE}.d8b{Fore.RESET} {Fore.CYAN}8d8b{Fore.RESET} {Fore.YELLOW}Yb  dP{Fore.RESET} {Fore.GREEN}88b.{Fore.RESET} {Fore.BLUE}w8ww{Fore.RESET} {Fore.CYAN}.d88b{Fore.RESET} {Fore.YELLOW}8d8b{Fore.RESET} 
{Fore.RED}8  8{Fore.RESET}  {Fore.MAGENTA}YbdP{Fore.RESET}  {Fore.BLUE}8{Fore.RESET}    {Fore.CYAN}8P{Fore.RESET}    {Fore.YELLOW}YbdP{Fore.RESET}  {Fore.GREEN}8  8{Fore.RESET}  {Fore.BLUE}8{Fore.RESET}   {Fore.CYAN}8.dP'{Fore.RESET} {Fore.YELLOW}8P{Fore.RESET}   
{Fore.RED}88P'{Fore.RESET}   {Fore.MAGENTA}dP{Fore.RESET}   {Fore.BLUE}`Y8P{Fore.RESET} {Fore.CYAN}8{Fore.RESET}      {Fore.YELLOW}dP{Fore.RESET}   {Fore.GREEN}88P'{Fore.RESET}  {Fore.BLUE}Y8P{Fore.RESET} {Fore.CYAN}`Y88P{Fore.RESET} {Fore.YELLOW}8{Fore.RESET}    
{Fore.RED}8{Fore.RESET}     {Fore.MAGENTA}dP{Fore.RESET}               {Fore.YELLOW}dP    {Fore.GREEN}8{Fore.RESET}                    
	
	""")
    print()
	
    try:
        path = argv[1]
		
        if not os.path.exists(path):
            print(f'[{Fore.RED}x{Fore.RESET}] Selected File {Fore.RED}NOT FOUND!{Fore.RESET}')
            exit()
        if not os.path.isfile(path) or not path.endswith('.py'):
            print(f'[{Fore.RED}x{Fore.RESET}] File Type {Fore.RED}INVALID!{Fore.RESET}')
            exit()
			
        with open(path, 'r', encoding='utf-8', errors='ignore') as file:
            file_content = file.read()
        pycrypt_content = pycrypt(file_content)
        with open(f'{path.split(".")[0]}_pycrypted.py', 'w') as file:
            file.write(pycrypt_content)
        print(f'[{Fore.GREEN}+{Fore.RESET}] File Has been PyCrypted {Fore.GREEN}SUCCESSFULLY!{Fore.RESET}')
    except:
        print(f'[{Fore.RED}x{Fore.RESET}] PyCrypter Correct Usage: {Fore.YELLOW}{argv[0]} <file>{Fore.RESET}')

if __name__ == '__main__':
    pycrypt_startup()

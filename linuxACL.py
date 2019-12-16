r"""
Usage example
for help
$ python linuxACL.py -h
"""

import argparse
import os

def greate():
    os.system('> file.txt')
    print('File is greate!')

def sets():
    #os.system('useradd admin')
    #print('User admin create')
    #os.system('useradd 
    #os.system('setfacl -m u:admin:rw-,u: file.txt')
    temp = os.popen('getfacl file.txt')
    for i in temp.read().split('\n')):
        if '# ' in i:
            i = i.replace('# ','')
        if len(i)==1:
            continue
        if ':' in i:
            print( i.split(':'))
        if '::' in i:
            print(i.split('::'))
            

def pars():
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Программа для парсинга данных ACL',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument("--greate", required=False, action="store_true",
                        help='Создать файл с правами')
    parser.add_argument("--sets", required=False, action="store_true", help='установить права')
    parser.add_argument('--pars', required=False, action='store_true',
                        help='Распарсить данные и вывести на экран')

    args = parser.parse_args()

    if args.greate:
        greate()

    elif args.sets:
        sets()
    elif args.pars:
        pars()

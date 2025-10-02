from banking import BankAccount
from log_utility import *
from jobs_implementation import *
from github import *
from cache_tools import ttl_cache
from git_commands_cli import *
import subprocess
import argparse
from concurrent_util import *
from time import sleep

@ttl_cache(seconds=5)
def add(a, b):
    print("Computing...")
    return a + b

if __name__ == "__main__":
    files_to_read = get_files_in_directory("D:\\MB_Prod_DB")

    acc = BankAccount("Bassel", 1000)

    son = BankAccount("Youssuf", 500)
    son.deposit(500)
    print(acc)

    #sleep(2)

    print(acc == son)
    print(len(acc))

    print(acc + son)
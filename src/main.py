import argparse

from email import parser
import sys

print("Hello from main.py!")

print(sys.argv)  # Print command-line arguments

parser.argparse.ArgumentParser(description="A simple command-line tool.")
parser.add_argument("--name", type=str, help="Your name")
parser.add_argument("--age", type=int, help="Your age") 

args = parser.parse_args()
if args.name:
    print(f"Hello, {args.name}!")

parser.add_argument("--age", choices=[str(i) for i in range(1, 101)], help="Your age between 1 and 100")
if args.age:
    print(f"You are {args.age} years old!")
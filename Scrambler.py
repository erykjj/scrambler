#!/usr/bin/env python3

"""
File:           Scrambler

Description:    Scramble the inner letters of words

MIT License     Copyright (c) 2022 Eryk J.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

VERSION = 'v0.0.1'


import random, argparse, re, string
from pathlib import Path


def scramble(word):
    if len(word) < 3:
        return word
    inner = list(word[1:-1])
    random.shuffle(inner)
    return word[0] + ''.join(inner) + word[-1]

def chunk(str):
    s = re.compile(r'\s')
    words = s.split(u''.join(c for c in str if c not in set(string.punctuation)))
    for word in words:
        wrod = scramble(word)
        str = str.replace(word, wrod, 1)
    return str

def main(args):
    print(f"\n*** {APP} {VERSION} ***")
    if args['Infile'] == args['Outfile']:
        print(f"\nPlease specify an output file that is different than the input file\n")
    else:
        with open(args['Infile'], 'r', encoding="UTF-8") as inf:
            with open(args['Outfile'], 'w', encoding="UTF-8") as outf:
                txt = inf.readline()
                outf.write(chunk(txt))
        print("\nCompleted successfully\n")


if __name__ == "__main__":
    PROJECT_PATH = Path(__file__).resolve().parent
    APP = Path(__file__).stem
    parser = argparse.ArgumentParser(description="Scramble inner letters of words")
    parser.add_argument('-v', '--version', action='version', version=f"{APP} {VERSION}")
    parser.add_argument("Infile", help='file to process')
    parser.add_argument("Outfile", help='output file')
    args = parser.parse_args()
    main(vars(args))
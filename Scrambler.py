#!/usr/bin/env python3

"""
File:           Scrambler

Description:    Scramble the inner letters of words

MIT License     Copyright (c) 2024 Eryk J.

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

VERSION = 'v0.0.3'

import random, argparse, re

def chunk(m, str):

    def scramble(match):
        word = match.group(1)
        inner = list(word[1:-1])
        random.shuffle(inner)
        return word[0] + ''.join(inner) + word[-1]

    return re.sub(m, scramble, str)

def main(args):
    print(f"\n*** {APP} {VERSION} ***")
    if args['Infile'] == args['Outfile']:
        print(f"\nPlease specify an output file that is different than the input file\n")
    else:
        m = re.compile(r'(\w{4,})')
        outf = open(args['Outfile'], 'w', encoding="UTF-8")
        with open(args['Infile'], 'r', encoding="UTF-8") as inf:
            txt = inf.readlines()
            for line in txt:
                outf.write(chunk(m, line))
        outf.close()
        print("\nCompleted successfully\n")

if __name__ == "__main__":
    APP = 'Scrambler'
    parser = argparse.ArgumentParser(description="Scramble inner letters of words")
    parser.add_argument('-v', '--version', action='version', version=f"{APP} {VERSION}")
    parser.add_argument("Infile", help='file to process')
    parser.add_argument("Outfile", help='output file')
    args = parser.parse_args()
    main(vars(args))
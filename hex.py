#!/usr/bin/env python3

import binascii
import argparse
import os
import sys

def encode():
    with os.fdopen(sys.stdin.fileno(), 'rb') as f:
        data = f.read()
    with os.fdopen(sys.stdout.fileno(), 'wb') as f:
        f.write(binascii.hexlify(data))

def decode():
    with os.fdopen(sys.stdin.fileno(), 'rb') as f:
        data = sys.stdin.read()
    with os.fdopen(sys.stdout.fileno(), 'wb') as f:
        f.write(binascii.unhexlify(data))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--decode', action='store_true')
    args = parser.parse_args()
    if args.decode:
        decode()
    else:
        encode()

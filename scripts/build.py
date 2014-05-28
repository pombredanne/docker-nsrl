# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
build.py
~~~~~~~~

This module builds a bloomfilter from the NSRL Whitelist Database.

:copyright: (c) 2014 by Josh "blacktop" Maine.
:license: GPLv3

"""

import os

from pybloomfilter import BloomFilter

error_rate = 0.01
nsrl_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'nsrl/NSRLFile.txt')


if os.path.isfile(nsrl_path):
    print "INFO: Reading in NSRL Database"
    hashes = [line.split(",")[1].strip('"') for line in open(nsrl_path)]
    print "INFO: Creating bloomfilter"
    bf = BloomFilter(len(hashes), error_rate, 'nsrl.bloom')
    print "INFO: Inserting hashes into bloomfilter"
    for a_hash in hashes[1:]:
        try:
            bf.add(a_hash)
        except Exception:
            print "ERROR !!"
    print "Complete"
else:
    print("ERROR: No such file or directory: '/nsrl/NSRLFile.txt'")
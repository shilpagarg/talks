#!/usr/bin/env python3
import random

l = 20
n = 8

def random_hap(l):
	return [random.sample(['0','0','1'], 1)[0] for i in range(l)]

haps = [random_hap(l) for i in range(n)]

for hap in haps:
	print(' '.join(str(x) for x in hap))


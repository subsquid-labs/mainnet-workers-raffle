#!/usr/bin/env python3

import sys
import numpy as np
import pandas as pd

seed = [ int(sys.argv[1][2:34], 16), int(sys.argv[1][34:], 16) ]

df = pd.read_csv('./finalPoints.csv')
sample = df.sample(
	n=133,
	replace=False,
	weights='score',
	axis=0,
	random_state=np.random.default_rng(seed=seed)
)
sample.to_csv('winners.csv', index=False)

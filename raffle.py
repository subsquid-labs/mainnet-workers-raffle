#!/usr/bin/env python3

import requests
import json
import numpy as np
import pandas as pd

seedHeight = 19558000 # expected to finalize April 1st, around 2AM UTC
rpcUrl = 'https://eth-mainnet.public.blastapi.io'

curHeightReply = requests.post(rpcUrl, json={'id': 0, 'jsonrpc': '2.0', 'method': 'eth_blockNumber'})
curHeight = int(json.loads(curHeightReply.text)['result'], 16)
if curHeight-seedHeight<80:
	raise RuntimeError(f'Seed block not finalized yet. You can wait a little longer, right?')

seedBlockReply = requests.post(rpcUrl, json={
	'id': 0,
	'jsonrpc': '2.0',
	'method': 'eth_getBlockByNumber',
	'params': [hex(seedHeight), False]
})
seedHash = json.loads(seedBlockReply.text)['result']['hash']

seed = [ int(seedHash[2:34], 16), int(seedHash[34:], 16) ]

df = pd.read_csv('./finalPoints.csv')
sample = df.sample(
	n=133,
	replace=False,
	weights='finalScore',
	axis=0,
	random_state=np.random.default_rng(seed=seed)
)
sample.to_csv('winners.csv', index=False)

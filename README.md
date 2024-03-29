Script and data for selecting Subsquid Network mainnet operators via a raffle.

Requires Pandas, NumPy and requests. In case your system is missing one of these packages, create a virtual environment and install them there:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

The script uses the hash of Ethereum block 19565000 as a random seed. The block is expected to finalize April 2nd, around 1.15AM UTC. If you run the script before that it'll throw an error.
```bash
python3 raffle.py
```


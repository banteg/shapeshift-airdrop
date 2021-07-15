import json
import csv
import glob
from decimal import Decimal

with open('airdrop.csv', 'wt') as f:
    writer = csv.writer(f)
    writer.writerow(['user', 'amount'])

    for path in glob.glob('proofs/0x*.json'):
        print(path)
        data = json.load(open(path))
        for user, info in data['claims'].items():
            writer.writerow([user, Decimal(int(info['amount'], 16)) / 10 ** 18])


import getpass
import hashlib
import sys

# storing only the HASH of your master password, not the password itself
MASTER_HASH = "e7c038f31f4a241001e57d95def669f1e5dd2e40a46c22b15fe65cac8c3dd03d"

entered = getpass.getpass("Master password: ")
if hashlib.sha256(entered.encode()).hexdigest() != MASTER_HASH:
    sys.exit()

PASSWORDS= {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
            'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
            'luggage': '12345'} 
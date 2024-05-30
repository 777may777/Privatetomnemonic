from bip_utils import Bip39MnemonicGenerator
import binascii
from tqdm import tqdm

def private_key_to_mnemonic(private_key_hex: str) -> str:
    # Convert the private key from hex to bytes
    private_key_bytes = binascii.unhexlify(private_key_hex)

    # Generate a seed from the private key
    seed = private_key_bytes.ljust(64, b'\0')  # Ensure the seed is 64 bytes long

    # Generate a BIP-39 mnemonic from the seed
    mnemonic = Bip39MnemonicGenerator().FromEntropy(seed[:32])
    return mnemonic

def read_private_keys(file_path: str):
    with open(file_path, 'r') as file:
        private_keys = file.readlines()
    # Remove any extra whitespace characters (like newline characters) from each key
    private_keys = [key.strip() for key in private_keys]
    return private_keys

def write_mnemonics(file_path: str, mnemonics: list):
    with open(file_path, 'w') as file:
        for mnemonic in mnemonics:
            file.write(mnemonic + '\n')

def main():
    private_keys = read_private_keys('private.txt')
    mnemonics = []

    # Using tqdm to create a progress bar
    for private_key in tqdm(private_keys, desc="Converting keys", unit="key"):
        try:
            mnemonic = private_key_to_mnemonic(private_key)
            mnemonics.append(mnemonic)
        except Exception as e:
            print(f"Error converting private key {private_key}: {e}")
            mnemonics.append(f"Error for key {private_key}")

    write_mnemonics('mne.txt', mnemonics)
    print("Conversion complete. Check mne.txt for the results.")

if __name__ == "__main__":
    main()

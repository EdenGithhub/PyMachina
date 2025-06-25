import os
import socket
import struct
import matplotlib.pyplot as plt
import numpy as np
from colorama import Fore, Style, init
from pyfiglet import figlet_format
import hexdump
from rich.console import Console
from rich.table import Table
import click
from tqdm import tqdm
from PIL import Image

init(autoreset=True)
console = Console()

class MachinaAnalyzer:
    def __init__(self, filepath):
        self.filepath = filepath
        self.header = None
        self.byte_data = b''
        self.parsed_data = []
        self.socket_data = None

    def read_file(self):
        if not os.path.isfile(self.filepath):
            console.print("[bold red]File not found!")
            return False
        with open(self.filepath, 'rb') as f:
            self.byte_data = f.read(512)
        self.header = self.byte_data[:2]
        console.print(f"[green]Header Detected:[/green] {self.header}")
        return True

    def show_header_ascii(self):
        print(Fore.CYAN + figlet_format("PyMachina"))
        print(Style.RESET_ALL + "File Signature:", self.header.decode(errors="ignore"))

    def show_hex(self):
        print(Fore.YELLOW + "Hex Dump of first 512 bytes:")
        hexdump.hexdump(self.byte_data)

    def visualize_bytes(self):
        arr = np.frombuffer(self.byte_data, dtype=np.uint8).copy()
        if len(arr) < 512:
            # Tambahkan 0 agar panjangnya 512
            arr = np.pad(arr, (0, 512 - len(arr)), 'constant')
        arr = arr.reshape((32, 16))
        plt.imshow(arr, cmap='plasma')
        plt.title("Binary Byte Structure")
        plt.colorbar()
        plt.show()


    def parse_struct(self):
        for i in range(0, len(self.byte_data), 4):
            chunk = self.byte_data[i:i+4]
            if len(chunk) == 4:
                val = struct.unpack('<I', chunk)[0]
                self.parsed_data.append(val)

    def display_struct_table(self):
        table = Table(title="Parsed DWORDs")
        table.add_column("Offset", justify="right")
        table.add_column("DWORD", justify="right")
        for i, val in enumerate(self.parsed_data):
            table.add_row(hex(i*4), hex(val))
        console.print(table)

    def socket_communicate(self, host='localhost', port=9999):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((host, port))
                s.sendall(b'HELLO FROM PyMachina')
                self.socket_data = s.recv(1024)
                console.print(f"[blue]Received:[/blue] {self.socket_data}")
        except ConnectionRefusedError:
            console.print("[bold red]Socket connection refused. Is the server running?")

    def image_bytes_visual(self):
        arr = np.frombuffer(self.byte_data, dtype=np.uint8).copy()
        if len(arr) < 512:
            arr = np.pad(arr, (0, 512 - len(arr)), 'constant')
        arr = arr.reshape((32, 16))
        img = Image.fromarray(np.uint8(arr))
        img = img.resize((160, 320)).convert('L')
        img.show()


    def progress_display(self):
        console.print("[bold cyan]Analyzing byte data...")
        for _ in tqdm(range(100), desc="Progress"):
            pass

    def reverse_bytes(self):
        reversed_data = self.byte_data[::-1]
        print(Fore.MAGENTA + "Reversed byte data (first 64 bytes):")
        print(reversed_data[:64])

    def save_parsed_to_txt(self, output_file='parsed_output.txt'):
        with open(output_file, 'w') as f:
            for i, val in enumerate(self.parsed_data):
                f.write(f"Offset {hex(i*4)}: {hex(val)}\n")
        console.print(f"[green]Parsed data saved to {output_file}")

    def analyze_entropy(self):
        from collections import Counter
        counter = Counter(self.byte_data)
        total = len(self.byte_data)
        entropy = -sum((count/total) * np.log2(count/total) for count in counter.values())
        console.print(f"[cyan]Entropy:[/cyan] {entropy:.4f} bits per byte")

    def show_byte_histogram(self):
        arr = np.frombuffer(self.byte_data, dtype=np.uint8)
        plt.hist(arr, bins=256, color='green', alpha=0.7)
        plt.title("Byte Frequency Histogram")
        plt.xlabel("Byte Value")
        plt.ylabel("Frequency")
        plt.grid(True)
        plt.show()

    def ascii_analysis(self):
        printable = ''.join(chr(b) if 32 <= b <= 126 else '.' for b in self.byte_data)
        print("ASCII View (printable chars):")
        print(printable)

    def ascii_frequency(self):
        freq = {}
        for b in self.byte_data:
            if 32 <= b <= 126:
                char = chr(b)
                freq[char] = freq.get(char, 0) + 1
        print("ASCII Character Frequency:")
        for k, v in sorted(freq.items()):
            print(f"{k}: {v}")

    def ascii_uppercase(self):
        print("Uppercase ASCII Characters:")
        print([chr(b) for b in self.byte_data if 65 <= b <= 90])

    def ascii_lowercase(self):
        print("Lowercase ASCII Characters:")
        print([chr(b) for b in self.byte_data if 97 <= b <= 122])

    def ascii_symbols(self):
        print("ASCII Symbols:")
        print([chr(b) for b in self.byte_data if 33 <= b <= 47])

    def ascii_digits(self):
        print("ASCII Digits:")
        print([chr(b) for b in self.byte_data if 48 <= b <= 57])

    def ascii_whitespace(self):
        print("Whitespace Characters:")
        print([chr(b) for b in self.byte_data if chr(b).isspace()])

    def ascii_isprintable(self):
        count = sum(1 for b in self.byte_data if chr(b).isprintable())
        print(f"Printable ASCII chars count: {count}")

    def utf8_decode_try(self):
        try:
            decoded = self.byte_data.decode('utf-8')
            print("UTF-8 Decoded:")
            print(decoded)
        except UnicodeDecodeError:
            print("Could not decode as UTF-8.")

    def utf8_find_non_utf(self):
        non_utf = [b for b in self.byte_data if b > 127]
        print("Non-ASCII (possible UTF-8 continuation bytes):")
        print(non_utf)

    def utf8_check_bom(self):
        if self.byte_data.startswith(b'\xef\xbb\xbf'):
            print("UTF-8 BOM Detected")
        else:
            print("No UTF-8 BOM")

    def run_full_analysis(self):
        if self.read_file():
            self.show_header_ascii()
            self.show_hex()
            self.visualize_bytes()
            self.parse_struct()
            self.display_struct_table()
            self.image_bytes_visual()
            self.progress_display()
            self.reverse_bytes()
            self.analyze_entropy()
            self.show_byte_histogram()
            self.save_parsed_to_txt()
            self.socket_communicate()
            self.ascii_analysis()
            self.ascii_frequency()
            self.ascii_uppercase()
            self.ascii_lowercase()
            self.ascii_symbols()
            self.ascii_digits()
            self.ascii_whitespace()
            self.ascii_isprintable()
            self.utf8_decode_try()
            self.utf8_find_non_utf()
            self.utf8_check_bom()

    def byte_sum(self):
        total = sum(self.byte_data)
        print(f"Total sum of bytes: {total}")

    def average_byte_value(self):
        avg = sum(self.byte_data) / len(self.byte_data) if self.byte_data else 0
        print(f"Average byte value: {avg:.2f}")

    def max_byte(self):
        max_val = max(self.byte_data) if self.byte_data else 0
        print(f"Max byte value: {max_val}")

    def min_byte(self):
        min_val = min(self.byte_data) if self.byte_data else 0
        print(f"Min byte value: {min_val}")

    def even_byte_count(self):
        even = sum(1 for b in self.byte_data if b % 2 == 0)
        print(f"Even byte count: {even}")

    def odd_byte_count(self):
        odd = sum(1 for b in self.byte_data if b % 2 != 0)
        print(f"Odd byte count: {odd}")

    def null_byte_count(self):
        nulls = self.byte_data.count(0)
        print(f"Null byte (\x00) count: {nulls}")

    def unique_byte_values(self):
        unique = set(self.byte_data)
        print(f"Unique byte values: {len(unique)}")

    def display_raw_bytes(self):
        print("Raw byte data (first 64 bytes):")
        print(self.byte_data[:64])

    def byte_value_counts(self):
        from collections import Counter
        counts = Counter(self.byte_data)
        common = counts.most_common(5)
        print("Top 5 most common byte values:")
        for byte, count in common:
            print(f"{byte}: {count} times")

    def run_full_analysis(self):
        if self.read_file():
            self.show_header_ascii()
            self.show_hex()
            self.visualize_bytes()
            self.parse_struct()
            self.display_struct_table()
            self.image_bytes_visual()
            self.progress_display()
            self.reverse_bytes()
            self.analyze_entropy()
            self.show_byte_histogram()
            self.save_parsed_to_txt()
            self.socket_communicate()
            self.ascii_analysis()
            self.ascii_frequency()
            self.ascii_uppercase()
            self.ascii_lowercase()
            self.ascii_symbols()
            self.ascii_digits()
            self.ascii_whitespace()
            self.ascii_isprintable()
            self.utf8_decode_try()
            self.utf8_find_non_utf()
            self.utf8_check_bom()
            self.byte_sum()
            self.average_byte_value()
            self.max_byte()
            self.min_byte()
            self.even_byte_count()
            self.odd_byte_count()
            self.null_byte_count()
            self.unique_byte_values()
            self.display_raw_bytes()
            self.byte_value_counts()        

@click.command()
@click.argument('filepath')
def main(filepath):
    analyzer = MachinaAnalyzer(filepath)
    analyzer.run_full_analysis()

if __name__ == '__main__':
    main()

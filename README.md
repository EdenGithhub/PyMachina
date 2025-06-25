# PyMachina

PyMachina is a powerful Python-based binary inspection and analysis tool that helps you extract, visualize, and understand the internal structure of low-level binary files such as `.exe`, `.bin`, `.hex`, and Arduino machine code.

It is ideal for:

* Reverse engineering learners
* Binary visualization enthusiasts
* Security researchers
* Hardware hackers and Arduino tinkerers

## Features

✅ ASCII, HEX, UTF-8 and byte-level analysis
✅ Entropy measurement for randomness analysis
✅ Struct parsing of 4-byte DWORDs (little-endian)
✅ Rich visualizations using matplotlib and image export
✅ Command-line interface with Click
✅ Socket testing support
✅ Terminal visuals using Colorama, PyFiglet, and Rich
✅ Uses over 10 powerful PyPI libraries

## Dependencies

PyMachina requires Python **3.7+**. Below are the key libraries used:

* `numpy`
* `matplotlib`
* `colorama`
* `pyfiglet`
* `hexdump`
* `rich`
* `click`
* `tqdm`
* `Pillow`
* `socket`, `struct`, `os` (standard libraries)

## Installation

1. Clone or download this repository to your desktop:

   ```bash
   git clone https://github.com/EdenGithhub/PyMachina.git
   cd PyMachina
   ```

2. Create virtual environment (recommended):

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Basic Command

```bash
python core.py "path/to/your/file.exe"
```

### Example

```bash
python core.py "C:/Users/ASPIRE/Desktop/sample.exe"
```

This will:

* Read first 512 bytes of the file
* Print the header in ASCII and HEX
* Parse the file into 4-byte chunks
* Display ASCII, symbols, digits, entropy, byte histogram
* Visualize the binary structure in both plots and grayscale image

### Help Menu

```bash
python core.py --help
```

## Sample Output

```
Header Detected: b'MZ'
 ____        __  __            _
|  _ \ _   _|  \/  | __ _  ___| |__
| |_) | | | | |\/| |/ _` |/ __| '_ \
|  __/| |_| | |  | | (_| | (__| | | |
|_|    \__, |_|  |_|\__,_|\___|_| |_|
       |___/

Hex Dump of first 512 bytes...
Entropy: 7.9964 bits per byte
Top 5 most common byte values:
  0: 12 times
  255: 9 times
  ...
```

## Notes

* PyMachina will pad any input smaller than 512 bytes.
* Socket support requires running a listening TCP server on `localhost:9999`
* Best used on `.exe`, `.bin`, `.hex`, or Arduino bootloader dumps

## License

MIT License

## Author

Created with ❤️ by [Eden Simamora]. Contributions welcome!
Contact :
    Email = aeden6877@gmail.com
    Github= EdenGithhub

© Eden/2025

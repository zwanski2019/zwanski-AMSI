import os
import ctypes
import ctypes.wintypes as wintypes
import logging

# Constants for AMSI
AMSI_RESULT_CLEAN = 0
AMSI_RESULT_NOT_DETECTED = 1
AMSI_RESULT_DETECTED = 32768

# Initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Load AMSI library
amsi = ctypes.WinDLL('amsi.dll')

# Initialize AMSI context
amsi.AmsiInitialize.argtypes = [wintypes.LPCWSTR, ctypes.POINTER(ctypes.c_void_p)]
amsi.AmsiInitialize.restype = wintypes.HRESULT
amsi_ctx = ctypes.c_void_p()
result = amsi.AmsiInitialize("MySecurityTool", ctypes.byref(amsi_ctx))
if result != 0:
    logging.error("Failed to initialize AMSI")
    exit(1)

# Function to scan a buffer
amsi.AmsiScanBuffer.argtypes = [ctypes.c_void_p, ctypes.c_void_p, wintypes.ULONG, wintypes.LPCWSTR, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
amsi.AmsiScanBuffer.restype = wintypes.HRESULT

def scan_file(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
    
    result = ctypes.c_int(AMSI_RESULT_CLEAN)
    amsi.AmsiScanBuffer(amsi_ctx, data, len(data), file_path, None, ctypes.byref(result))
    
    if result.value == AMSI_RESULT_DETECTED:
        logging.warning(f"Malicious content detected in {file_path}")
    else:
        logging.info(f"{file_path} is clean or not detected")

# Function to scan all files in a directory
def scan_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            logging.info(f"Scanning {file_path}")
            scan_file(file_path)

# Directory to scan
directory_to_scan = "C:\\path\\to\\directory"

# Scan the directory
scan_directory(directory_to_scan)

# Uninitialize AMSI context
amsi.AmsiUninitialize.argtypes = [ctypes.c_void_p]
amsi.AmsiUninitialize.restype = None
amsi.AmsiUninitialize(amsi_ctx)

logging.info("AMSI scanning completed")

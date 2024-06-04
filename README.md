# Zwanski-AMSI

![Zwanski-AMSI](https://via.placeholder.com/800x200?text=Zwanski-AMSI)

Zwanski-AMSI is an advanced security tool designed to integrate with the Windows Antimalware Scan Interface (AMSI) for detecting malicious content in files. This tool is particularly useful for security researchers, ethical hackers, and system administrators who need to perform thorough security assessments and scans within their environments.

## Features

- **AMSI Integration**: Leverages the Windows AMSI for real-time scanning and detection of malicious content.
- **Recursive Directory Scanning**: Capable of scanning all files within a specified directory, including subdirectories, ensuring comprehensive coverage.
- **Detailed Logging**: Utilizes the Python `logging` module to provide detailed logs of scanning activities, detections, and overall results.
- **Automated Detection**: Automatically detects and logs files identified as malicious, helping users quickly identify potential threats.
- **Flexible Configuration**: Easy to modify and extend for additional functionalities or integrations with other security tools.

## Usage

1. **Initialization**: The tool initializes the AMSI context, preparing it for scanning operations.
2. **File Scanning**: Reads the content of each file in the specified directory and submits it to AMSI for scanning.
3. **Result Logging**: Logs the results of each scan, indicating whether the content is clean or potentially malicious.
4. **Completion**: Uninitializes the AMSI context after completing the scan, ensuring clean resource management.

```bash
python3 zwanski_amsi.py

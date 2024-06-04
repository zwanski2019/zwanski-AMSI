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

``bash
python3 zwanski_amsi.py

Configuration
Directory to Scan: Set the directory_to_scan variable to the path of the directory you wish to scan.
Logging Level: Adjust the logging level as needed (INFO, WARNING, ERROR) to control the verbosity of log messages.
Prerequisites
Windows operating system
Python 3.x
AMSI.dll available on the system
Disclaimer
Zwanski-AMSI is intended for authorized use only. Ensure you have explicit permission to scan any files or directories targeted by this tool. The end user is responsible for complying with all applicable laws and regulations.

Installation and Setup
git clone https://github.com/yourusername/zwanski-amsi.git
cd zwanski-amsi
Install required Python packages:
pip install -r requirements.txt
Configure the directory to scan by editing the directory_to_scan variable in the script.

Run the script:
python3 zwanski_amsi.py
Zwanski-AMSI is a powerful tool for enhancing your cybersecurity posture, providing detailed insights into potential threats through seamless AMSI integration. Use it responsibly and ethically to contribute to a safer digital environment.



You can now copy and paste this content directly into your `README.md` file on GitHub.

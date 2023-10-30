import subprocess
import socket
import logging

def get_logger(name: str):
    return logging.getLogger(f"[{socket.gethostname()}] {name}")

def run_shell_command(cmd: str):
    return subprocess.run(cmd, text=True, shell=True, check=True, capture_output=True).stdout


# utils.py

import platform
import subprocess


def ping_ip(ip):
    # ip = "192.168.0.103"
    current_os = platform.system()
    params = "-n"
    if current_os == "Windows":
        params = "-n"
    elif current_os == "Linux":
        params = "-c"
    try:
        result = subprocess.run(["ping", params, "1", "-w", "500", ip], stdout=subprocess.PIPE)  # 执行ping命令，发送一个ICMP包
        if result.returncode == 0:
            # status = 0
            status = True
        else:
            # status = -1
            status = False
    except subprocess.CalledProcessError as e:
        result = f"Ping failed: {e.output}"
        # status = -1
        status = False

    return status


def turn_off_pc(ip, account):
    result = subprocess.run(
        [
            "ssh",
            "-o",
            "UserKnownHostsFile=/dev/null",
            "-o",
            "StrictHostKeyChecking=no",
            "-i",
            "/home/suping/.ssh/id_rsa",
            f"{account}@{ip}",
            "shutdown",
            "/s",
            "/t",
            "60",
        ],
        capture_output=True,
        text=True,
    )

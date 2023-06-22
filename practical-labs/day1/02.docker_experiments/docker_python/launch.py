"""Main file to launch processes from"""

import os
import time
import subprocess

JUPYTER_PASSWORD = os.environ.get("JUPYTER_PASSWORD", "")

print("This script starts a Jupyter Lab server and puts it in the background")
cmd = ["jupyter", "lab", "--no-browser", "--allow-root", "--ip=0.0.0.0", f"--NotebookApp.token={JUPYTER_PASSWORD}"]
proc = subprocess.Popen(
    cmd,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE, 
    text=True
)

while proc.poll() is None:
    print("JupyterLab should be available at http://localhost:8888")
    time.sleep(15*60)

"""Development-only polling reloader for the single-file reference app."""
import signal
import subprocess
import sys
import time
from pathlib import Path


def stop(child):
    if child.poll() is None:
        child.terminate()
        try:
            child.wait(timeout=5)
        except subprocess.TimeoutExpired:
            child.kill()
            child.wait()


def shutdown(signum, frame):
    raise SystemExit(0)


if __name__ == "__main__":
    signal.signal(signal.SIGTERM, shutdown)
    signal.signal(signal.SIGINT, shutdown)
    source = Path("app.py")
    previous = source.read_bytes()
    child = subprocess.Popen([sys.executable, "-u", "app.py"])
    try:
        while True:
            time.sleep(0.5)
            try:
                current = source.read_bytes()
            except FileNotFoundError:
                continue  # Some editors replace a file through a temporary rename.
            if current != previous:
                previous = current
                print("app.py changed; restarting application", flush=True)
                stop(child)
                child = subprocess.Popen([sys.executable, "-u", "app.py"])
    finally:
        stop(child)

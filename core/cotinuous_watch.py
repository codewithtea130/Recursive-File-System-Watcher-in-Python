from core.take_snapshot import get_snapshot
from core.store_sanpshot import store_snapshot
from core.compare import compare_folder
import time


def start_loop(folder):
    scan_count = 0
    try:
        print("Scanning...")
        previous_snapshot = get_snapshot(folder)
        while True:
            current_snapshot = get_snapshot(folder)
            result = compare_folder(current_snapshot, previous_snapshot)
            previous_snapshot = store_snapshot(current_snapshot)
            scan_count += 1
            time.sleep(2)

    except KeyboardInterrupt:
        print("Watcher Stopped")

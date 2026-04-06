from core.get_input import get_path
from core.take_snapshot import get_snapshot
from core.store_sanpshot import store_snapshot
from core.cotinuous_watch import start_loop


def main():
    folder = get_path()
    start_loop(folder)


if __name__ == "__main__":
    main()

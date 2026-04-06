from pathlib import Path


def get_snapshot(folder_path):
    root_folder = Path(folder_path)

    snap_shot = {}

    all_items = [root_folder] + list(root_folder.rglob("*"))

    for item in all_items:
        try:
            stat = item.stat()
            size = stat.st_size
            mtime = stat.st_mtime

            item_info = {
                "path": str(item),
                "name": item.name,
                "type": "folder" if item.is_dir() else "file",
                "size": size,
                "mtime": mtime,
            }

            snap_shot[str(item)] = item_info

        except (PermissionError, FileNotFoundError):
            continue

    return snap_shot

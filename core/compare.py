from core.show_result import show_result


def compare_folder(current_snapshot, previous_snapshot):
    new_paths = set(current_snapshot.keys())
    old_paths = set(previous_snapshot.keys())

    common_paths = new_paths & old_paths

    created_paths = new_paths - old_paths

    deleted_paths = old_paths - new_paths

    modified_paths = set()

    rename_paths = []

    created_items_info = []
    deleted_items_info = []
    modified_items_info = []

    matched_deleted = set()
    matched_created = set()

    for path in common_paths:
        old_info = previous_snapshot[path]
        new_info = current_snapshot[path]

        if (
            new_info["mtime"] != old_info["mtime"]
            or new_info["size"] != old_info["size"]
        ):
            modified_paths.add(path)

    for old_path in deleted_paths:
        old_info = previous_snapshot[old_path]

        for new_path in created_paths:
            new_info = current_snapshot[new_path]

            if old_info["type"] != new_info["type"]:
                continue

            if old_info["size"] != new_info["size"]:
                continue

            diff = abs(old_info["mtime"] - new_info["mtime"])

            if diff > 1:
                continue

            rename_paths.append(
                {
                    "old_path": old_path,
                    "new_path": new_path,
                    "type": new_info["type"],
                    "name": new_info["name"],
                }
            )
            matched_deleted.add(old_path)
            matched_created.add(new_path)
            break

    new_deleted_paths = deleted_paths - matched_deleted
    new_created_paths = created_paths - matched_created

    for new_created_path in new_created_paths:
        created_items_info.append(current_snapshot[new_created_path])

    for new_deleted_path in new_deleted_paths:
        deleted_items_info.append(previous_snapshot[new_deleted_path])

    for modified_path in modified_paths:
        modified_items_info.append(current_snapshot[modified_path])

    changes = {
        "created": created_items_info,
        "deleted": deleted_items_info,
        "modified": modified_items_info,
        "renamed": rename_paths,
    }

    show_result(changes)

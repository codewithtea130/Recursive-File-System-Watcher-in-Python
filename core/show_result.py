from datetime import datetime


def show_result(changes):
    # print("changes", changes)
    created_items = changes["created"]
    deleted_items = changes["deleted"]
    modified_items = changes["modified"]
    renamed_items = changes["renamed"]

    event_time = datetime.now().strftime("%Y:%m:%d %H:%M%S")

    for created_item in created_items:
        print(
            f"[{event_time}] {created_item['type']} {created_item['name']} created : {created_item['path']}"
        )
    for deleted_item in deleted_items:
        print(
            f"[{event_time}] {deleted_item['type']} {deleted_item['name']} deleted : {deleted_item['path']}"
        )
    for modified_item in modified_items:
        print(
            f"[{event_time}] {modified_item['type']} {modified_item['name']} modified : {modified_item['path']}"
        )
    for renamed_item in renamed_items:
        print(
            f"[{event_time}] {renamed_item['type']} {renamed_item['name']} renamed : {renamed_item['old_path']} to {renamed_item["new_path"]}"
        )
    if (
        not created_items
        and not deleted_items
        and not modified_items
        and not renamed_items
    ):
        print(f"[{event_time}] No changes detected.")

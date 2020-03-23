import math


def find_current_most_valuable_lib(current_task, day_left, current_running_libraries):
    total_timing_results = []
    for lib_id, lib in enumerate(current_task.libraries):
        if lib_id in current_running_libraries:
            continue
        unique_book_ids = sorted([i for i in range(len(lib.books_ids)) if not current_task.books[i].is_scanned],
                                 key=lambda j: current_task.books[j].score, reverse=True)
        amount_of_books_until_end = lib.scanning_throughput*(day_left-lib.signup_time) \
            if lib.scanning_throughput*(day_left-lib.signup_time) <= len(lib.books_ids) else len(lib.books_ids)
        value = sum(unique_book_ids[:amount_of_books_until_end])
        total_timing_results.append((value, lib_id))
    if len(total_timing_results) == 0:
        return -1
    current_most_valuable_lib = sorted(total_timing_results, key= lambda x: x[0], reverse=True)[0][1]
    return current_most_valuable_lib

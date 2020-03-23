import math


def find_current_most_valuable_lib(current_task, day_left):
    total_timing_results = []
    for lib_id, lib in enumerate(current_task.libraries):
        unique_book_ids = sorted([i for i in range(len(lib.books_ids)) if not lib.books_ids[i].is_scanned],
                                 key=lambda j: lib.books_ids[j].score, reverse=True)
        amount_of_books_until_end = lib.scanning*(day_left-lib.signup_time) \
            if lib.scanning*(day_left-lib.signup_time) <= len(lib.books_ids) else len(lib.books_ids)
        value = sum(unique_book_ids[:amount_of_books_until_end])
        total_timing_results.append((value, lib_id))
    current_most_valuable_lib = sorted(total_timing_results, key= lambda x: x[0], reverse=True)[0][1]
    return current_most_valuable_lib

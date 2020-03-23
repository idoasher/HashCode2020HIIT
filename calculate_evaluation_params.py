import math


def find_current_most_valuable_lib(current_task, day_left):
    total_timing_results = []
    for lib in current_task.libraries:
        unique_book_ids = sorted([i for i in range(len(lib.books_ids)) if not lib.books_ids[i].is_scanned], key=lalib.books_ids[i], reverse=True)

        """
        unique_book_ids = [lib.books_ids[i] for i in range(len(lib.books_ids)) if not lib.books_ids[i].is_scanned]
        book_scoring_array = [current_task.books[i].score for i in unique_book_ids]
        total_book_score = sum(book_scoring_array)
        total_scanning_time = math.ceil(len(book_scoring_array) / lib.scanning_throughput)
        total_lib_time = total_scanning_time + lib.signup_time
        total_timing_results.append(total_book_score / total_lib_time)
        """
    current_most_valuable_lib = list(reversed(sorted((e, i) for i, e in enumerate(total_timing_results))))[0][1]
    return current_most_valuable_lib

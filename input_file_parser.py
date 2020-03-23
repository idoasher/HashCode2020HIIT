import task_setting
import book
import library


def parse(input_file_path):
    with open(input_file_path, "r") as input_file:
        books_count, libraries_count, days = (int(x) for x in input_file.readline().split(' '))
        # print books_count, libraries_count, days
        books = [book.Book(book_id, score) for (book_id, score) in enumerate(input_file.readline().split(' '))]
        # for b in books:
        #    print b.id, b.score
        libraries_data_lines = input_file.readlines()
        # print libraries_data_lines
        libraries = []
        for lib_id in range(libraries_count):
            number_of_books, signup_time, scanning_throughput = (int(x) for x in
                                                                 libraries_data_lines[2 * lib_id].split(' '))
            # print number_of_books, signup_time, scanning_throughput
            books_ids = [int(x) for x in libraries_data_lines[2 * lib_id + 1].split(' ')]
            libraries.append(library.Library(lib_id, signup_time, scanning_throughput, books_ids))
        # for lib in libraries:
        #     print lib.id, lib.signup_time, lib.scanning_throughput, lib.books_ids
        return task_setting.TaskSetting(books_count, libraries_count, days, libraries, books)


# for testing:
if __name__ == '__main__':
    parse("InputFiles\\a_example.txt")
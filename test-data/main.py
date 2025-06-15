"""Json and CSV parser"""
import csv
import json


def read_books(filename: str) -> list:
    """CSV reader with delimiter ',' """
    with open(filename, encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=',')
        books = []
        for row in reader:
            books.append({
                'title': row['Title'].strip(),
                'author': row['Author'].strip(),
                'pages': int(row['Pages']),
                'genre': row['Genre'].strip()
            })
        return books


def read_users(filename: str) -> list:
    """Json reader"""
    with open(filename, encoding='utf-8') as file:
        raw_users = json.load(file)
        users = []
        for user in raw_users:
            users.append({
                'name': user.get('name'),
                'gender': user.get('gender'),
                'address': user.get('address'),
                'age': user.get('age'),
                'books': []
            })
        return users


def distribute_books(users: list, books: list) -> list:
    """Distribution of book between users
    index % amount_of_users - helps to distribute books evenly among users"""
    amount_of_users = len(users)
    for index, book in enumerate(books):
        users[index % amount_of_users]['books'].append(book)
    return users


def save_result(data: list, filename: str) -> None:
    """Saving results to Json file"""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def main():
    """Main function of the program"""
    books = read_books('books.csv')
    users = read_users('users.json')
    result = distribute_books(users, books)
    save_result(result, 'result.json')


if __name__ == '__main__':
    main()

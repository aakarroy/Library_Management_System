
# Nexus of Knowledge Library Management System

Welcome to the Nexus of Knowledge Library Management System! This Python-based application manages various operations within the library, such as reading books, issuing books, returning books, and more. 

## Features

1. **Read Books**: Allows users to select and read books from various categories available in the library.
2. **Return Books**: Enables users to return borrowed books.
3. **Issue Books**: Allows users to issue books for a period of time.
4. **Return Issued Books**: Users can return books they have issued.
5. **Donate Books**: Allows users to donate books to the library.
6. **Exit**: Option to exit the application.

## Getting Started

### Prerequisites

- Python 3.x
- MySQL server
- MySQL Connector for Python (`mysql-connector-python`)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/NexusOfKnowledge.git
   ```

2. Install the required Python packages:

   ```bash
   pip install mysql-connector-python
   ```

3. Set up your MySQL database:

   - Create a MySQL database named `aakar`.
   - Set up the required tables:
     - `CUSTOMER_DETAILS`
     - `TABLE_NUMBER`
     - `book_types`
     - `library`
     - `issued_books`
     - `donated_books`

4. Update the database connection details in the script:

   ```python
   con = c.connect(host='localhost', password="xyz@1234", user="root", database="aakar")
   ```

## Usage

1. Run the main script:

   ```bash
   python main.py
   ```

2. Follow the prompts to interact with the library system.

### Functionalities

- **Reading Books**: Choose from various book categories and get a book delivered to your table.
- **Returning Books**: Return books you have borrowed and free up the occupied table.
- **Issuing Books**: Issue books to read at home, with an option to return them within 10 days.
- **Returning Issued Books**: Return books you've issued and retrieve your security deposit.
- **Donating Books**: Donate books to the library, and the system will check for duplicates.


## Acknowledgements

- MySQL Connector for Python
- Python Regular Expressions (re module)
- Python `datetime` module


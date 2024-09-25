# Library Management System

## Project Overview

This project is a **Library Management System** that allows administrators to manage books, members, and transactions (book issues and returns). The application features an intuitive interface for recording and managing the library's operations, including the calculation of fees for overdue book returns.

## Features

- **Book Management**: Add, update, and delete books in the library's inventory.
- **Member Management**: Register new members, update member information, and track member debt.
- **Transaction Handling**: 
  - Issue books to members.
  - Return books and automatically calculate fees based on the duration of the issue.
  - Track the history of transactions for each member.
- **Fee Calculation**: A fee is calculated for each day a book is overdue, with a maximum debt limit of 500 KES.

## Tech Stack

- **Python** (Flask) - Backend Framework
- **Jinja2** - Template Engine for dynamic HTML
- **SQLite** Database for storing library data
- **HTML/CSS** - Frontend
- **Bootstrap** - UI framework for styling

## Project Setup

### Prerequisites

- Python 3.x
- Virtualenv (recommended)
- Git

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Mosesomo/library-management.git
    cd library-management
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```


4. Run the application:

    ```bash
    python3 app.py
    ```

5. Visit the application in your browser at `http://127.0.0.1:5000/`.

### Folder Structure

```bash
library-management-system/
├── system/
│   ├── __init__.py
│   ├── models.py         # Models for Book, Member, and Transaction
│   ├── routes.py         # Application routes
│   ├── static/           # Static files (CSS, JS)
│   └── templates/        # HTML templates
├── README.md             # Project documentation
├── requirements.txt      # Python dependencies
└── app.py                # Entry point to run the Flask app

# Here are the Screen shots
## Books Layout
![image](https://github.com/user-attachments/assets/7cbe4239-4f84-4ade-a477-8c3c4565b64a)

## Add book
![image](https://github.com/user-attachments/assets/412470dd-9ba3-4325-be00-d297065d1dc1)

## Members layout
![image](https://github.com/user-attachments/assets/21957a0c-f61b-4e4b-b5a6-1f5fee7a54b2)

## Add Member
![image](https://github.com/user-attachments/assets/4ab8a963-f611-474b-9413-b4d08cd03d5c)

## Delete Member
![image](https://github.com/user-attachments/assets/df06d854-c6ad-4b73-bb28-28e60f41d22a)

## Transaction (issueing of the book)
![image](https://github.com/user-attachments/assets/7f5651e3-32c7-43c3-8bda-71ce3e377b6c)

## Add transaction
![image](https://github.com/user-attachments/assets/f326ec16-e26d-42a7-9503-f78a66a72c98)


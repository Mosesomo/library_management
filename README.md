
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

![Screenshot (211)](https://github.com/user-attachments/assets/451193db-eb07-49e6-92f7-5265bbcaf6fe)
![Screenshot (210)](https://github.com/user-attachments/assets/88f56c70-51c5-413f-80be-144ad76d4ab5)
![Screenshot (209)](https://github.com/user-attachments/assets/b713c34b-4c1b-474d-b159-eaaed07277d0)
![Screenshot (208)](https://github.com/user-attachments/assets/a98eb03e-fbdb-4daf-9f2a-76327e5c927f)
![Screenshot (207)](https://github.com/user-attachments/assets/25908c27-265c-4984-b096-08d67d95d3c0)![Screenshot (219)](https://github.com/user-attachments/assets/6c1f61b1-c549-4e77-9768-b71564e27064)
![Screenshot (218)](https://github.com/user-attachments/assets/67ab0371-6b22-4870-994c-0edd8a5c1d71)
![Screenshot (217)](https://github.com/user-attachments/assets/251d9b81-9cea-4405-a94d-5f357e78b7d6)
![Screenshot (216)](https://github.com/user-attachments/assets/2570fa6f-3671-4c5d-b24e-6492c11a97e5)
![Screenshot (215)](https://github.com/user-attachments/assets/3ad9ea35-399a-4a27-92b2-43e3d867cec1)
![Screenshot (214)](https://github.com/user-attachments/assets/e15ffc6b-3022-4ab9-9d34-e2104b1ba91d)
![Screenshot (213)](https://github.com/user-attachments/assets/b8aea481-f50d-4328-9332-fd2ea184b463)
![Screenshot (212)](https://github.com/user-attachments/assets/235bf9a9-5903-4dec-84d6-359f306cb1ff)



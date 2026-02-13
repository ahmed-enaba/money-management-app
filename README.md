# 💰 Money Management System (Python)

A simple **Money Management System** built using **Python** and **SQLite** that helps users track their income and expenses efficiently through a command-line interface.


## 📌 Features

- ✅ Add income
- ❌ Deduct expenses
- 📊 View total balance
- 📝 Show transaction history with reasons and dates
- 💾 Data stored locally using SQLite database
- 🖥️ Simple and beginner-friendly CLI interface


## 🛠️ Technologies Used

- **Python 3**
- **SQLite3**
- **Datetime module**


## 📂 Project Structure
money-management/
│
├── money_management.py
├── money_management.db  (created automatically)
└── README.md

## ▶️ How to Run

1. Make sure Python 3 is installed on your machine.
2. Open terminal or command prompt.
3. Navigate to the project folder.
4. Run the following command:


## 🧠 How It Works

- The program creates a SQLite database named:
  `money_management.db`
- It creates a table called:
  `money_management`
- Each transaction stores:
  - Amount
  - Reason
  - Date
- The total balance is calculated using SQL SUM() function.

## 📋 Example Menu

Welcome to Money Management App

1 - Show Balance  
2 - Add Money  
3 - Deduct Money  
4 - Show Reasons  
5 - Exit  


## 🚀 Future Improvements

- Add graphical user interface (GUI)
- Add user authentication
- Export transactions to CSV file
- Add monthly and yearly financial reports
- Add input validation and error handling


## 👨‍💻 Author

Ahmed  
Computer Science Student  
Interested in Backend Development and Automation

## 📄 License

This project is open-source and free to use for educational purposes.

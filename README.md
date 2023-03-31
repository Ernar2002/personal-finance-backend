# Personal Finance Tracker
**Personal Finance Tracker** is a simple and easy-to-use application designed to help users manage and track their personal finances. 
Users can create custom categories for income and expenses, set up multiple wallets, and monitor all transactions in a user-friendly interface.

### Features
* Create and manage multiple wallets
* Add custom income and expense categories
* Record transactions (incomes and expenses) with descriptions and dates
* Categorize transactions for better organization and tracking
* View wallet balance and transaction history

### Getting Started
These instructions will help you set up the Personal Finance Tracker on your local machine for development and testing purposes.


### Installation

1. Clone the repository to your local machine:

```console
git clone https://github.com/username/personal-finance-tracker.git
cd personal-finance-tracker
```

2. Make sure you have Docker installed on your machine. If not, please follow the [official Docker installation guide](https://docs.docker.com/get-docker/).


3. Build and run the application using Docker Compose:

```console
docker compose up --build
```


The application will now be running on [http://localhost:8000](http://localhost:8000). You can access the API documentation at [http://localhost:8000/docs](http://localhost:8000/docs).

## Technologies Used
- Python 3.11.1
- FastAPI - A modern, fast, web framework for building APIs with Python
- SQLAlchemy - The Python SQL Toolkit and Object-Relational Mapper
- Alembic - A database migration tool for SQLAlchemy
- Docker - A platform for developing, shipping, and running applications in containers


## License
This project is licensed under the MIT License - see the [LICENSE](https://chat.openai.com/LICENSE) file for details.
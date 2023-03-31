from models import Transaction
from schemas import (TransactionCreate, TransactionUpdate)
from .base import ServiceBase


class TransactionService(ServiceBase[Transaction, TransactionCreate, TransactionUpdate]):
    pass


transaction_service = TransactionService(Transaction)

from models import Wallet
from schemas import (WalletCreate, WalletUpdate)
from .base import ServiceBase


class WalletService(ServiceBase[Wallet, WalletCreate, WalletUpdate]):
    pass


wallet_service = WalletService(Wallet)

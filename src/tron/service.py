from tronpy import Tron
from .schemas import TronInfo
from .repository import TronRepository


class TronService:
    def __init__(self, tron_repository: TronRepository):
        self.tron_repository = tron_repository

    def get_tron_info(self, address: str) -> TronInfo:
        # Получаем информацию с использованием tronpy
        client = Tron()
        trx_balance = client.get_account_balance(address)
        resources = client.get_account_resource(address)
        # Предполагаем, что bandwidth и energy берутся из ключей "free_net_limit" и "energy_limit"
        bandwidth = resources.get("free_net_limit", 0)
        energy = resources.get("energy_limit", 0)
        # Записываем запрос в БД
        self.tron_repository.create_request(address)
        return TronInfo(
            address=address, trx_balance=trx_balance, bandwidth=bandwidth, energy=energy
        )

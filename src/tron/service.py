from tronpy.async_tron import AsyncTron
from .schemas import TronInfo
from .repository import TronRepository


class TronService:
    def __init__(self, tron_repository: TronRepository):
        self.tron_repository = tron_repository
        self.client = AsyncTron(network="nile")

    async def get_tron_info(self, address: str) -> TronInfo:
        if not self.client.is_address(address):
            raise ValueError("Invalid TRON address format")

        try:
            trx_balance = await self.client.get_account_balance(address)
            resources = await self.client.get_account_resource(address)
        except Exception as e:
            if "account not found" in str(e):
                trx_balance, resources = 0, {"free_net_limit": 0, "energy_limit": 0}
            else:
                raise e

        bandwidth = resources.get("free_net_limit", 0)
        energy = resources.get("energy_limit", 0)

        await self.tron_repository.create_request(address)

        return TronInfo(
            address=address, trx_balance=trx_balance, bandwidth=bandwidth, energy=energy
        )

    async def close(self):
        await self.client.close()

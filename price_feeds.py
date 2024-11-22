from gql import gql

class PriceFeeds:
    def __init__(self, uni_client, chainlink_contract):
        self.uni_client = uni_client
        self.chainlink_contract = chainlink_contract

    async def get_uniswap_price(self) -> float:
        query = gql("""
            {
                pool(id: "0x8ad599c3a0ff1de082011efddc58f1908eb6e6d8") {
                    token0Price
                }
            }
        """)
        try:
            data = await self.uni_client.execute_async(query)
            return float(data['pool']['token0Price'])
        except Exception as e:
            return None

    async def get_chainlink_price(self) -> float:
        try:
            round_data = self.chainlink_contract.functions.latestRoundData().call()
            return float(round_data[1]) / 10**8  # Цена в USD
        except Exception:
            return None

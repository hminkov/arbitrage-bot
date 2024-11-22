class FlashbotsExecutor:
    def __init__(self, w3, account):
        self.w3 = w3
        self.account = account

    async def execute_bundle(self, transactions):
        try:
            # Изпращане на Flashbots bundle
            bundle = [{"signed_transaction": tx.rawTransaction} for tx in transactions]
            response = await self.w3.flashbots.send_bundle(bundle)
            return response['status'] == 1
        except Exception as e:
            return False

class OpenRouterContextOptimizerClient:
    def optimize(self, context_messages: list[dict], limit_tokens: int) -> dict:
        return {"optimized_messages": context_messages[-3:]}
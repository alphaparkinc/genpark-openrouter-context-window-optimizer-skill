from client import OpenRouterContextOptimizerClient
client = OpenRouterContextOptimizerClient()
print(client.optimize([{"role": "user", "text": "hello"}]*10, 4000))
import requests

def build_quote(inputMint, outputMint, amount):
    url = f'https://quote-api.jup.ag/v6/quote?inputMint={inputMint}&outputMint={outputMint}&amount={amount}'
    return url


def get_quote(quote):
    quote = requests.get(quote)
    print(quote.json())


inputMint = 'So11111111111111111111111111111111111111112'
outputMint = 'JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN'
amount = 10000

quote = build_quote(inputMint, outputMint, amount)
get_quote(quote)

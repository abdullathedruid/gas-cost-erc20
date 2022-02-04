import json
from brownie import interface

GAS_SAVINGS = {
    "approve": 42565 - 42519,
    "transfer": 31945 - 31875,
    "transferFrom": 20442 - 20400,
}
WETH = interface.WETH


def main():
    cumul_gas = 0
    cumul_tx = 0
    data = json.load(open("bigquery.json", "r"))
    # print(data)
    selectors = [func for func in data if func["sig_hash"] in WETH.selectors]
    for sel in selectors:
        func = WETH.selectors[sel["sig_hash"]]
        if func in GAS_SAVINGS:
            gwei = float(sel["gwei"])
            gas = GAS_SAVINGS[func]
            print(
                f"{gwei:.3f} Gwei/gas spent on performing {func}(). Each function saves {gas} gas"
            )
            total_saving = gas * gwei / 1e9
            cumul_gas += total_saving
            cumul_tx += int(sel["f0_"])
            print(f"Total ETH saved by {func}(): {total_saving:.3f}")
            print("--")
    print(f"Total ETH saving across all functions: {cumul_gas:.3f} ")
    print(f"Total number of transactions: {cumul_tx}")

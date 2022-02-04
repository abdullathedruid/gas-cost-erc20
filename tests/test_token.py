from brownie import accounts
from brownie.test import given, strategy


@given(
    value=strategy("uint256", max_value=2**255 - 1),
    _from=strategy("address"),
    _to=strategy("address"),
    _sender=strategy("address"),
)
def test_approve_and_transfer(safe_token, unsafe_token, value, _from, _to, _sender):
    safe_token.mint(_from, value, {"from": _from})
    safe_token.transfer(_to, value, {"from": _from})
    safe_token.mint(_from, value, {"from": _from})
    safe_token.approve(_sender, value, {"from": _from})
    safe_token.transferFrom(_from, _to, value, {"from": _sender})
    unsafe_token.mint(_from, value, {"from": _from})
    unsafe_token.transfer(_to, value, {"from": _from})
    unsafe_token.mint(_from, value, {"from": _from})
    unsafe_token.approve(_sender, value, {"from": _from})
    unsafe_token.transferFrom(_from, _to, value, {"from": _sender})

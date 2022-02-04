from vyper.interfaces import ERC20

implements: ERC20

event Transfer:
    sender: indexed(address)
    receiver: indexed(address)
    value: uint256

event Approval:
    owner: indexed(address)
    spender: indexed(address)
    value: uint256

name: public(String[64])
symbol: public(String[32])
decimals: public(uint8)

balanceOf: public(HashMap[address, uint256])
allowance: public(HashMap[address, HashMap[address, uint256]])
totalSupply: public(uint256)


@external
def __init__(_name: String[64], _symbol: String[32], _decimals: uint8):
    self.name = _name
    self.symbol = _symbol
    self.decimals = _decimals
    self.totalSupply = 0



@external
def transfer(_to : address, _value : uint256) -> bool:
    assert _to != ZERO_ADDRESS # dev: ERC20: transfer to the zero address
    assert msg.sender != ZERO_ADDRESS # dev: ERC20: transfer from the zero address
    assert _to != self # dev: ERC20: transfer to contract address
    self.balanceOf[msg.sender] -= _value
    self.balanceOf[_to] += _value
    log Transfer(msg.sender, _to, _value)
    return True


@external
def transferFrom(_from : address, _to : address, _value : uint256) -> bool:
    assert _to != ZERO_ADDRESS # dev: ERC20: transfer to the zero address
    assert _from != ZERO_ADDRESS # dev: ERC20: transfer from the zero address
    assert _to != self # dev: ERC20: transfer to contract address
    self.balanceOf[_from] -= _value
    self.balanceOf[_to] += _value
    self.allowance[_from][msg.sender] -= _value
    log Transfer(_from, _to, _value)
    return True


@external
def approve(_spender : address, _value : uint256) -> bool:
    assert msg.sender != ZERO_ADDRESS # dev: ERC20: approve from the zero address
    assert _spender != ZERO_ADDRESS # dev: ERC20: approve to the zero address
    self.allowance[msg.sender][_spender] = _value
    log Approval(msg.sender, _spender, _value)
    return True


@external
def mint(_to: address, _value: uint256):
    # this function is only being used for testing
    self.totalSupply += _value
    self.balanceOf[_to] += _value
    log Transfer(ZERO_ADDRESS, _to, _value)
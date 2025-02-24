from models.user import User, db
from datetime import datetime, timezone

def test_user_instantiaton():
    eth_addr = "0x1234567890abcdef1234567890abcdef12345678"
    marvel_username = "TestPlayer"
    user = User(eth_address=eth_addr, marvel_username=marvel_username)

    assert user.eth_address == eth_addr
    assert user.marvel_username == marvel_username
    assert isinstance(user.created_at, datetime)
    assert user.last_login is None
    assert user.nonce is None

def test_user_default_values():
    eth_addr = "0x1234567890abcdef1234567890abcdef12345678"
    user = User(eth_address=eth_addr)

    assert user.marvel_username is None
    assert isinstance(user.created_at, datetime)
    assert user.last_login is None
    assert user.nonce is None





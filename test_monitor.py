from monitor import hash_file


def test_hash_file():
  assert hash_file('sample.txt') == '5891b5b522d5df086d0ff0b110fbd9d21bb4fc7163af34d08286a2e846f6be03'

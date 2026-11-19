from monitor import hash_file, scan_folder


def test_hash_file():
  assert hash_file('sample.txt') == '5891b5b522d5df086d0ff0b110fbd9d21bb4fc7163af34d08286a2e846f6be03'

def test_scan_folder_atxt():
  assert scan_folder('test_folder/a.txt') == {'test_folder/a.txt': 'b6a98d9ce9a2d9149288fa3df42d377c3e42737afdcdaf714e33c0a100b51060'}

def test_scan_folder_btxt():
  assert scan_folder('test_folder/sub/b.txt') == {'test_folder/sub/b.txt': '5da8f23decf397b13f4f55b6fb8a61936238bfe08ed9d901132974f1beccc45c'}

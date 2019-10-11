# Python Secret Storage package
Secret data is encrypted using your public RSA-key and stored in the ".store" folder. 
The keys should be located in the "~/.ssh/" folder.
For decryption, a secret key is used from the same folder. 
Data must be a <class 'bytes'>.

## Install
```bash
pip install kan_secret_storage
```

## Usage
```python
import kan_secret_storage.main as ss

message = 'Hello Blablacode.ru!'
ss.storedata("message", message.encode("utf-8"))
message1 = ss.getdata("message")
```

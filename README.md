# secret_storage
Python Secret Storage package

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
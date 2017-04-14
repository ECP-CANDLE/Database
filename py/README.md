
## Setup

1. Install pip

2. Do `pip install requests`

3. Download PySolr:
```
wget https://pypi.python.org/packages/47/d6/91dd269b4443c77905ac5f347318435bfeaa2825ce2763d936e0945f29e4/pysolr-3.6.0.tar.gz
```

4. Untar it

5. Set `PYTHONPATH` to include the directory `pysolr-3.6.0` or copy `pysolr.py` into `PYTHONPATH` somewhere

## Insert from command line

```
./run_insert.py <run_id> <parameters>
```

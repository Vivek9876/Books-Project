## Initialize
 
Clone this repository
Run following command from the root of this directory
 
Initialize [venv](https://docs.python.org/3/library/venv.html)
 
Execute following commands to download dependencies
 
```shell
pip install -r requirements.txt
```
 
Execute following commands to clear dependencies
 
```shell
pip uninstall -y -r requirements.txt
```

## Start server
 
```shell
python uvicorn app.main:app --reload 
```
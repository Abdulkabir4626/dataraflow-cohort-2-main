import sys, pathlib
_p = pathlib.Path.cwd()
while _p != _p.parent and not (_p / "dataraflow_db.py").exists():
    _p = _p.parent 
sys.path.insert(0,str(_p))     
from dataraflow_db import run_query
print(run_query("SELECT 1 as test"))
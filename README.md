Timing info for a function. </br>
### USAGE
1) 
```
pip install git+https://github.com/melih1996/timer.git
```
2) 
```
from time import sleep
from timer import Timer
with Timer("your title"):
    sleep(12)
```
gives "your title : 12 seconds, 12ms"
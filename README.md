## Bagel

Import python scripts over the web!

**Doesn't check if it is a real python script, do not feed it a RANDOM website. It will bite.**

### Installation

**Linux/MacOS**
```bash 
python -m pip install git+https://github.com/Bod-Studios/Bagel.git@main
python -m pip install colored
```
**Windows**
```bash
py -m pip install git+https://github.com/Bod-Studios/Bagel.git@main
py -m pip install colored
```

### Basic Usage
```python
from bagel import webImport

MYFILE = WebImport("https://someurl.com/funscript.py")

```

### Example

```python
from bagel import webImport


test = webImport("https://pastebin.com/raw/rtTstHLB")


hi = test.Hello()

```

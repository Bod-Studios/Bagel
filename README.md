## Bagel

Import python scripts over the web!

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/t/bod-inc/Bagel)

**Doesn't check if it is a real python script, do not feed it a RANDOM website. It will bite.**

### Installation

**Linux/MacOS**
```bash 
python -m pip install git+https://github.com/Bod-Studios/Bagel.git@main#egg=bagel
```
**Windows**
```bash
py -m pip install git+https://github.com/Bod-Studios/Bagel.git@main#egg=bagel
```

### Basic Usage & Edit Config
```python
from bagel import webImport

MYFILE = WebImport("https://someurl.com/funscript.py")

import bagel
bagel.config.ConfigObject = Config Object -> you create

```

### Example

```python
from bagel import webImport


test = webImport("https://pastebin.com/raw/rtTstHLB")


hi = test.Hello()

```


### Example 2
#### With webExport()

```python
from bagel import webImport 
test = webImport("https://pastebin.com/raw/EyPw4KUn")

print(test)
```


### Building from Source

**It** is very basic, all you need todo is `pip install -e .`





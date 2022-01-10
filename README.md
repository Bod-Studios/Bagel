## Bagel

Import python scripts over the web!

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

### Building from Source

**It** is very basic, all you need todo is `pip install -e .`
in main directoy, *has src & setup.py*
If cloning the source code, VSCode says there is a ERROR in webImport.py ignore it. The function requires its self as a parameter, and VSCode doesn't recognize it and flags it as an error. It runs just fine!


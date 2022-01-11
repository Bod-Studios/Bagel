from functools import wraps

import requests

from ..util import Failure, Ok, Reset, Sucsess, debug


# Thank you stack overflow
def withself(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        return f(f, *args, **kwds)
    return wrapper


def webImport( url: str):
    data = requests.get(url).text
    
    @withself
    def returnFunc(self):
        funcs = {}
        exec(data, {'__builtins__':__builtins__}, funcs) # type: ignore
        debug(f"{Sucsess}Executed Data{Reset}")
        setattr(self, "funcs", funcs)
        return self
    
    # Function Object
    
    # flake8: noqa
    FUNC = returnFunc()     # type: ignore

    

    for func in FUNC.funcs.items():
            # Can go through multipe because self.funcs 
            if not hasattr(FUNC.funcs, str(func[0])):
                debug(f"{Sucsess}{func[0]}{Reset}")
                # Setting the Atribute of this class -> The FUNCTION with the body of the functiion  
                setattr(FUNC, str(func[0]), FUNC.funcs.get(func[0]))
                # exec(f"FUNC.{func}")

    # Check if webExport exsists and then return it instead of something else
    if hasattr(FUNC, "webExport"):
        return FUNC.webExport()
    return FUNC

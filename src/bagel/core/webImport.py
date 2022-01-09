from ..util import debug, Sucsess, Failure, Ok, Reset
import requests
from functools import wraps


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
        exec(data, {'__builtins__':__builtins__}, funcs)
        debug(f"{Sucsess}Executed Data{Reset}")
        setattr(self, "funcs", funcs)
        return self
    
    # Function Object
    FUNC = returnFunc()

    for func in FUNC.funcs.items():
            # Can go through multipe because self.funcs 
            if not hasattr(FUNC.funcs, str(func[0])):
                debug(f"{Sucsess}{func[0]}{Reset}")
                # Setting the Atribute of this class -> The FUNCTION with the body of the functiion  
                setattr(FUNC, str(func[0]), FUNC.funcs.get(func[0]))
                # exec(f"FUNC.{func}")

    return FUNC





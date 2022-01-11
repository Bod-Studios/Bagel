from ..config import ConfigObject


def debug(object):
    if ConfigObject.debug == True:
        try: 
            # Determine if __.debug exsits for message
            print(object.__debug)

        except AttributeError:
            print(object)
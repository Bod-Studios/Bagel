import uuid
class Config:
    """Config Class for Copying to create the configuration object for bagel, can be left blank!
    """
    def __init__(self):
        self.debug = False # Change for Production
        self.gpu = False
        self.cpu = True
        self.id = str(uuid.uuid4())
        

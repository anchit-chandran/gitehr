class RecordWriter:
    """
    Returns a markdown-formatted string, to be written to a GitEHR Record file.
    """
    
    def __init__(self, contents:str="", separator="\n", sign=True):
        self.contents=contents
        self.separator=separator
    
    def add_line(self, content:str)->None:
        self.contents+=content+self.separator
        
    def add_contents(self, _contents_lst:list[str])->None:
        _contents_joined = "\n".join(_contents_lst)
        self.add_line(_contents_joined)
    
    def add_public_key(self)->None:
        
        self.add_contents([
            "\n",
            "-----BEGIN PGP PUBLIC KEY BLOCK-----",
            "mQINBFRUAGoBEACuk6ze2V2pZtScf1Ul25N2CX19AeL7sVYwnyrTYuWdG2FmJx4x",
            "=nUop",
            "-----END PGP PUBLIC KEY BLOCK-----",
            ])
    
    def get_contents(self)->str:
        self.add_public_key()
        return self.contents


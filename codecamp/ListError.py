class AddError(Exception):
    """Exception raised for errors in the function Add

    Parameters
    ----------
    message : str
        message of the error
    """
    def __init__(self, message = "AddError"):
        self.message = message
        print(self.message)

class ModifyError(Exception):
    """Exception raised for errors in the function Modify

    Parameters
    ----------
    message : str
        message of the error
    """
    def __init__(self, expression="ModufyErr0r", message = "ModifyError"):
        self.message = message
        self.expression = expression
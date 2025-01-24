def last(*args):
    if len(args) == 1:
        if isinstance(args[0], (list, str)):
            return args[0][-1]  
        else:
            return args[0]  
    else:
        return args[-1] 


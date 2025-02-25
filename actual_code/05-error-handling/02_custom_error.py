class UOEError(Exception):  # class UoEError extends Exception:
    pass

try:
    raise UOEError()
except UOEError:
    print("This was an error from UoE - find on line ...")
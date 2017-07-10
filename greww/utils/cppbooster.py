import ctypes
from greww.greww.utils.exception import CppImportException

Types= {'int' : ctypes.c_int,
         'char' : ctypes.c_char,
         'string' : ctype.c_char_p}



def call_cpp_function(func, path=None, out_put=None, in_put=None, op=None):
    if path is None:
        pass
    try:
        module = ctypes.CDLL(path)
    except:
        raise CppImportException(path)
    try:
        function = module.func
    except:
        raise CppFunctionImport(func, path)

    if out_put: function.restype = Types[out_put] if type(out_put) == str else out_put
    if in_put: function.argstypes = Types[in_put] if type(in_put) == str else in_put

    return function


def call_cpp_object(obj, path=None):
    pass





# call_cpp_function(ked, path="/Users/ial/greww/greww/settings.so", out_put=ctypes.c_char_p)
"""
settings = ctypes.CDLL("/Users/ial/greww/greww/settings.so")
a=settings.ked
a.restype=ctypes.c_char_p
print(a)

print(a())
"""

import math
import os
import psutil

# units
def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1000)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

# inner psutil function
def process_memory():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss

# decorator function
def profile(func):
    def wrapper(*args, **kwargs):
 
        mem_before = process_memory()
        result = func(*args, **kwargs)
        mem_after = process_memory()
        print("{}:consumed memory: {} {} {}".format(
            func.__name__,
            convert_size(mem_before), convert_size(mem_after), convert_size(mem_after - mem_before)))
 
        return result
    return wrapper

# an example without decorator
mem_before = process_memory()
# executed section
mem_after = process_memory()
print("consumed memory: {} {} {}".format(
    convert_size(mem_before), convert_size(mem_after), convert_size(mem_after - mem_before)))

def tracer(func):
    depth = 0
    
    def wrapper(*args, **kwargs):
        nonlocal depth
        
        indent = "|  " * depth
        args_repr = ", ".join([repr(arg) for arg in args])
        if kwargs:
            kwargs_repr = ", ".join([f"{k}={repr(v)}" for k, v in kwargs.items()])
            full_args = f"{args_repr}, {kwargs_repr}" if args_repr else kwargs_repr
        else:
            full_args = args_repr
        
        print(f"{indent}{func.__name__}({full_args})")
        
        depth += 1
        result = func(*args, **kwargs)
        depth -= 1
        
        print(f"{indent}-> {func.__name__}({full_args}) = {repr(result)}")
        
        return result
    
    return wrapper


# if __name__ == "__main__":
#     @tracer
#     def factorial(n):
#         if n <= 1:
#             return 1
#         return n * factorial(n - 1)
    
#     factorial(3)
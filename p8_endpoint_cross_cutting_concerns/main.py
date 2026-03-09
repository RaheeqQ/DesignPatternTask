#decorator method
def authentication(handler):
    # *args collects all positional arguments into a tuple test(1, 2, 3).
    # **kwargs collects all keyword arguments into a dictionary test(name="Ali", age=20).
    def wrapped(*args, **kwargs):
        print("Validating auth")
        result = handler(*args, **kwargs)
        print("authentication ended successfully")
        return result
    return wrapped


def rate_limit(handler):
    def wrapped(*args, **kwargs):
        print("Checking rate limits")
        result = handler(*args, **kwargs)
        print("Checking rate limits ended successfully")
        return result
    return wrapped

def log(handler):
    def wrapped(*args, **kwargs):
        print("Logging request")
        result = handler(*args, **kwargs)
        print("Logging ended successfully")
        return result
    return wrapped

@authentication
@rate_limit
@log
def handle_request():
    print("Processing request")


if __name__ == '__main__':
    handle_request()
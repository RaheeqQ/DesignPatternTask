#decorator method
class RESTHandler:
    def handle_request(self):
        pass


class AuthenticationHandler(RESTHandler):
    def __init__(self, wrapped):
        self._wrapped = wrapped
    def handle_request(self):
        print("Validating auth")
        self._wrapped.handle_request()


class RateLimitsHandler(RESTHandler):
    def __init__(self, wrapped):
        self._wrapped = wrapped
    def handle_request(self):
        print("Checking rate limits")
        self._wrapped.handle_request()


class LogHandler(RESTHandler):
    def __init__(self, wrapped):
        self._wrapped = wrapped
    def handle_request(self):
        print("Logging request")
        self._wrapped.handle_request()


class ProcessHandler(RESTHandler):
    def handle_request(self):
        print("Processing request")


if __name__ == '__main__':
    handle = AuthenticationHandler(RateLimitsHandler(LogHandler(ProcessHandler())))
    handle.handle_request()
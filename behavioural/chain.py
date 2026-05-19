# Imagine a Technical Support Phone System. Your call first goes to an automated bot (Level 1). If the bot can't solve your issue, it passes the call to a human technician (Level 2). If the technician is stumped, they escalate it to a senior engineer (Level 3). The request travels down a chain until someone is qualified to handle it.

class Handler:
    def __init__(self, level):
        self.level = level
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler

    def handle(self, request):
        if self.can_handle(request):
            print(f"Handled by {self.__class__.__name__}")
        elif self.next_handler:
            self.next_handler.handle(request)
        else:
            print("No handler available for this request.")

    def can_handle(self, request):
        return request <= self.level
class Level1Handler(Handler):
    def __init__(self):
        super().__init__(level=1)
class Level2Handler(Handler):
    def __init__(self):
        super().__init__(level=2)
class Level3Handler(Handler):
    def __init__(self):
        super().__init__(level=3)
# Usage Example
if __name__ == "__main__":
    level1 = Level1Handler()
    level2 = Level2Handler()
    level3 = Level3Handler()

    level1.set_next(level2)
    level2.set_next(level3)

    requests = [0, 1, 2, 3, 4]  # Different levels of requests
    for req in requests:
        print(f"Processing request with level {req}:")
        level1.handle(req)
        print("-" * 30)
# Output:
# Processing request with level 0:  
# Handled by Level1Handler
# ------------------------------    
# Processing request with level 1:
# Handled by Level1Handler
# ------------------------------
# Processing request with level 2:
# Handled by Level2Handler
# ------------------------------
# Processing request with level 3:
# Handled by Level3Handler
# ------------------------------
# Processing request with level 4:
# No handler available for this request.


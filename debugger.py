class Debugger:
    def __init__(self, on: bool):
        self.flag_count = 0
        self.prefix = "[DEBUGGER]\t"
        self.on = on
    
    def set_flag(self, label=""):
        if not self.on:
            return
        if not label:
            print(self.prefix + str(self.flag_count))
        else:
            print(self.prefix + str(self.flag_count) + " " + label)
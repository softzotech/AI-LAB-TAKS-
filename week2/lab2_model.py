class Controller:
    def __init__(self):
        self.last = "none"

    def decide(self, temp, people):
        if people == 0:
            mode = "eco"
        elif temp >= 27:
            mode = "cool"
        elif temp <= 19:
            mode = "heat"
        else:
            mode = "off"
        if mode == self.last:
            send = "no"
        else:
            send = "yes"
            self.last = mode
        return mode, send

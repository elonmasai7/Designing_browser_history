class BrowserHistory(object):

    def __init__(self, homepage):
        self.history = [homepage]
        self.current = 0

    def visit(self, url):
        self.history = self.history[:self.current + 1]
        self.history.append(url)
        self.current += 1

    def back(self, steps):
        self.current = max(0, self.current - steps)
        return self.history[self.current]

    def forward(self, steps):
        self.current = min(len(self.history) - 1, self.current + steps)
        return self.history[self.current]


browserHistory = BrowserHistory("leetcode.com")
browserHistory.visit("google.com")
browserHistory.visit("facebook.com")
browserHistory.visit("youtube.com")
print(browserHistory.back(1)) 
print(browserHistory.back(1)) 
print(browserHistory.forward(1)) 
browserHistory.visit("linkedin.com")
print(browserHistory.forward(2))  
print(browserHistory.back(2))  
print(browserHistory.back(7))  

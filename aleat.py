#!/usr/bin/python3

import webapp


class URLAleatApp(webapp.webApp):  #esto significa que URLAleatApp va a heredar de webApp

    def process(self, parsedRequest):
        import random
        return ["200 OK", "<html><body><h1><a href = '" + str(random.randint(1,10000000)) + "'>Dame otra</a></h1></body></html>"]
           
if __name__ == "__main__":
    testWebApp = URLAleatApp("localhost", 1234)
                
           

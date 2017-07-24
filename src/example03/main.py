import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

class CountHandler(webapp2.RequestHandler):
    def get(self):
        for i in range(1, 21):
            self.response.write('Hello %d <br>' % i)

class GoodbyeHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Goodbye!')

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/count', CountHandler),
    ('/goodbye', GoodbyeHandler)
], debug=True)

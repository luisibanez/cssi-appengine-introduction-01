import webapp2
import logging

class MainHandler(webapp2.RequestHandler):
    def get(self):
        logging.info('Printing hello message')
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

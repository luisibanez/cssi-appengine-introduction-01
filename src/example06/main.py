import webapp2
import logging


def is_prime(n):
    """A simple (but inefficient) check to see whether a number is prime."""
    for possible_factor in range(1, n):
        logging.info('trying %d' % possible_factor)
        if n % possible_factor == 0:
            return False
    return True

class MainHandler(webapp2.RequestHandler):
    def get(self):
        n = 100
        if is_prime(n):
            self.response.write('%d is prime' % n)
        else:
            self.response.write('%d is not prime' % n)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

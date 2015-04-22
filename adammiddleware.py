# import shortuuid
import random
from django.db import connection

__doc__ = '''
  Middleware classes for the site.
'''

###################################################
###   GUIDs to be used as unique ids in different
###   elements on the page.
###   - Based off of island.byu.edu code by Conan Albrecht

class WebGuidMiddleware:
  '''Attaches a web-valid guid generator to each request'''

  ### generate web id via a callable class
  def process_request(self, request):
    request.generator = WebIdGenerator()


  ### generate web id via a generator function
  # def __init__(self):
  #   self.generator = get_next()

  # def process_request(self, request):
    # add the generator to the request
    # request.generator = self.generator


class WebIdGenerator(object):
  '''A callable class that returns the next web-valid guid in the sequence for the given request.
     Don't use this class directly.  Instead, call this with something like:

       wid = request.get_unique_id()

    I purposely didn't use a generator for this because I want a normal method call syntax
    to be consistent with the rest of the class.
  '''
  def __init__(self):
    # a base_guid and a counter ensures 1) speed and 2) unique guids are created throughout the request
    self.counter = 0
    self.base_guid = None

  def __call__(self):
    # we generate the guid late because many requests don't need one
    if self.base_guid == None:
      self.base_guid = random.randrange(10000, 99999) #took out shortuuid.uuid()
    self.counter += 1

    # get a unique value from the sequence in the database
    cursor = connection.cursor()
    cursor.execute("SELECT nextval('webidsequence')")
    dbSequence = cursor.fetchone()[0]

    return 'a%s%x%s' % (self.base_guid, self.counter, dbSequence)  # start with arbitrary letter a because element ids must start with a letter



### generator function
# def get_next():
#   i=0
#   while True:
#     #create the next unique id and yield it
#     i+=1
#     yield "a" + str(i) + str(random.randrange(10000, 99999))

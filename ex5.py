class DocumentState(object):

   name = "state"
   allowed = []

   def switch(self, state):
      """ Switch to new state """
      if state.name in self.allowed:
         print("Current state:",self," => ",self.comment[self.allowed.index(state.name)],"=> switched to new state:",state.name)
         self.__class__ = state
      else:
         print("Current state:",self," => switching to",state.name,"not possible.")

   def __str__(self):
      return self.name

class Draft(DocumentState):
   name = "draft"
   allowed = ["moderation","published"]
   comment = ["Published by user","Published by admin"]

class Moderation(DocumentState):
   name = "moderation"
   allowed = ["draft","published"]
   comment = ["Review failed","Approved by admin"]

class Published(DocumentState):
   name = "published"
   allowed = ["draft"]
   comment = ["Publication expired"]

class Document(object):
   
   def __init__(self,):
      self.state = Draft()
   
   def change(self, state):
      """ Change state """
      self.state.switch(state)

if __name__ == "__main__":
   doc = Document()
   doc.change(Draft)
   doc.change(Moderation)
   doc.change(Draft)
   doc.change(Published)
   doc.change(Draft)
   doc.change(Moderation)
   doc.change(Published)
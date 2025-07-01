from recordclass import RecordClass

class Session(RecordClass):
    learned = ""
    '''What was learned'''
    seconds = 0
    '''How long it lasted'''
    date = 0
    '''Unix Timestamp.'''


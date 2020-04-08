class Exam(object):
    def __init__(self, title, description, long_description):
        self.title = title
        self.description = description
        self.long_description = long_description
        
    def __repr__(self):
        return(
            u'Exam(title={}, description={})'
            .format(self.title, self.description)
        )

class Question(object):
    def __init__(self, examId, question, image):
        self.examId = examId
        self.question = question
        self.image = image

    def __repr__(self):
        return(
            u'Question(examId={}, question={}, image={})'
            .format(self.examId, self.question, self.image)
        )
    
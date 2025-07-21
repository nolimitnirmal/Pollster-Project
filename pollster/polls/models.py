from django.db import models

# Create your models here.

class Question(models.Model):  # this model represents a poll question
    question_text = models.CharField(max_length=200) # it has a text field for the question
    pub_date = models.DateTimeField('date published')   # and a date field for when it was published

# the model creates an id automatically and itw ill be used as the primary key and it is auto incremented by default
    # auto-incremented means that each time a new question is created, it will get a unique id automatically

    def __str__(self): # this fundtion returns the string that represents the Question object
        # when we print a Question object, it will return the question_text
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # this creates a foreign key relationship with the Question model. a foreign key to the primary key of the Question model
    #on_delete=models.CASCADE means that if the question is deleted, all its choices will also be deleted
    choice_text = models.CharField(max_length=200)  # it has a text field
    votes = models.IntegerField(default=0)  # it has a field for the number of votes, default is 0

    def __str__(self): 
        return self.choice_text

from django import forms
from .models import Question, Comment


# Question Form
class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('title', 'subject', 'text',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Setting the materialize css form classes
        for field in self.Meta.fields:
            if field == 'title':
                self.fields[field].widget.attrs.update({
                    'class': 'validate'
                })
            if field == 'text':
                self.fields[field].widget.attrs.update({
                    'class': 'materialize-textarea'
                })


# Comment Form
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Setting the materialize css form classes
        for field in self.Meta.fields:
            self.fields[field].widget.attrs.update({
                'class': 'materialize-textarea'
                })

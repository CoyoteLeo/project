from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class Todolistform(forms.Form):
    uid = forms.IntegerField(widget=forms.HiddenInput)
    title = forms.CharField(label='*Title', min_length=3, help_text='At least 3 words', required=False,)
    content = forms.CharField(label='Content', required=False)
    remind_date = forms.DateField(label='RemindDate', help_text='If blank,it\'ll be a event without deadline.', required=False,
                                  widget=DateInput(attrs={'required': False}))
    finish_or_not = forms.BooleanField(label='Finish?', required=False, initial=False)

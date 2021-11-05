from django import forms
from .models import Rsvp


class RsvpFrom(forms.ModelForm):
  class Meta:
    model = Rsvp
    fields = ('name','furi','tel','post','address','mail','message','allergy','conpanion1','conpanion2','conpanion3',)

  def __init__(self, *args, **kwags):
    super().__init__(*args, **kwags)
    self.fields['name'].widget.attrs = {'placeholder':'名前'}
    self.fields['furi'].widget.attrs = {'placeholder':'ふりがな'}
    self.fields['tel'].widget.attrs = {'placeholder':'080-0000-0000'}
    self.fields['post'].widget.attrs = {'placeholder':'870-0000'}
    self.fields['address'].widget.attrs = {'placeholder':'大分県大分市○○番地○○号'}
    self.fields['mail'].widget.attrs = {'placeholder':'info@example.com'}
    self.fields['allergy'].widget.attrs = {'placeholder':'例：卵、魚介、小麦'}
    self.fields['conpanion1'].widget.attrs = {'placeholder':'名前'}
    self.fields['conpanion2'].widget.attrs = {'placeholder':'名前'}
    self.fields['conpanion3'].widget.attrs = {'placeholder':'名前'}


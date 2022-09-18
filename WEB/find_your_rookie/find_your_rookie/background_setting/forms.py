from socket import fromshare
from django import forms

class ForwardForm(forms.Form):
    goals = forms.BooleanField(label='goals', required=False)
    SpG = forms.BooleanField(label='SpG', required=False)
    Drb = forms.BooleanField(label='Drb', required=False)
    Assists = forms.BooleanField(label='Assists', required=False)
    KeyP = forms.BooleanField(label='KeyP', required=False)
       
class MidfielderForm(forms.Form):
    PSper = forms.BooleanField(label='PS%', required=False)
    Crosses = forms.BooleanField(label='Crosses', required=False)
    LongB = forms.BooleanField(label='LongB', required=False)
    Assists = forms.BooleanField(label='Assists', required=False)
    KeyP_ThrB = forms.BooleanField(label='KeyP/ThrB', required=False)
    
class DefenderForm(forms.Form):
    Tackles = forms.BooleanField(label='Tackles', required=False)
    Interc = forms.BooleanField(label='Interc', required=False)
    Clear = forms.BooleanField(label='Clear', required=False)
    Blocks = forms.BooleanField(label='Blocks', required=False)
    Offsides = forms.BooleanField(label='Offsides', required=False)
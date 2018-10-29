from django import forms
from BankApp.models import Login,Register

Account_Type = (
    ('SB',  'Saving'),
    ('LB','Loan'),
    ('IB','Insurance'),

)
Insurance_Type = (
    ('vechle',  'vechle'),
    ('Home','Home'),
    ('personal','personal'),

)
Loan_Type = (
    ('car',  'car'),
    ('Home','Home'),
    ('personal','personal'),

)
Transcation_id=(
    ('W','withdrawn'),
    ('D','deposite')
)





class LoginForm(forms.Form):
    customerName=forms.CharField(max_length=25)
    password = forms.CharField(required=True, label='Password', max_length=32, widget=forms.PasswordInput())
    '''
    class Meta:
        model = Login
        fields = '__all__'
    '''

class RegisterForm(forms.ModelForm):
    #userName = forms.CharField(max_length=25)
    password = forms.CharField(required = True,label = 'Password',max_length = 32,widget = forms.PasswordInput())
    #Age=forms.IntegerField()
    imgfile = forms.ImageField(label='Choose your image', help_text='The image should be cool.')

    class Meta:
        model=Register
        fields='__all__'
#bal,type,customer
class Account_Register(forms.Form):
    customer=forms.IntegerField()
    accountBalance=forms.FloatField()
    customerName=forms.CharField(max_length=15)
    #Age=forms.IntegerField()
    accountType=forms.ChoiceField(choices=Account_Type, widget=forms.RadioSelect())

class Account_Info(forms.Form):
    id=forms.IntegerField()

class Insurance_Register(forms.Form):
    Name=forms.CharField(max_length=15)
    Age = forms.IntegerField()
    iType = forms.ChoiceField(choices=Insurance_Type, widget=forms.RadioSelect())

class Loan_Register(forms.Form):
    Name=forms.CharField(max_length=15)
    Age = forms.IntegerField()
    lType = forms.ChoiceField(choices=Loan_Type, widget=forms.RadioSelect())


class Withdrawn_Deposite(forms.Form):
    accountNumber = forms.IntegerField()
    transactionAmount=forms.IntegerField()
    transactionMethod = forms.ChoiceField(choices=Transcation_id, widget=forms.RadioSelect())





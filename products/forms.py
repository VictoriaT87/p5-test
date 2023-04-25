from django import forms
from .models import Games


class GamesForm(forms.ModelForm):

    class Meta:
        model = Games
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        # create tuple list of friendly namea
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        # set each fields name as friendly name
        self.fields['category'].choices = friendly_names
        # add class to each field name
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
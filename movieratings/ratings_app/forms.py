from django import forms

from .models import Rating

class RatingForm(forms.ModelForm):

    class Meta:
        model = Rating
        fields = ('rating_value', 'review')

    def clean_rating_value(self):
        data = self.cleaned_data['rating_value']
        if data in range(1,6):
            return data
        else:
            raise forms.ValidationError("Rating {} out of bounds (1-5).".format(data))

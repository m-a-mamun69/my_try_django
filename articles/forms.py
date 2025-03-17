from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    # def clean_title(self):
    #     cleaned_data = self.cleaned_data
    #     print("Cleaned Data: ", cleaned_data)
    #     title = cleaned_data.get('title')
    #     if title.lower().strip() == "Title Two":
    #         raise forms.ValidationError('This Title Is Taken.')
    #     print("Title: ", title)
    #     return title
    
    def clean(self):
        cleaned_data = self.cleaned_data
        # print("All Data: ", cleaned_data)
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if title.lower().strip() == "title two":
            self.add_error('title', 'This Title Is Taken.')
            # raise forms.ValidationError('This Title Is Taken.')
        if "two" in content or "two" in title.lower():
            self.add_error('content', 'Office cannot be in content')
            raise forms.ValidationError('Office is not allowed.')
        return cleaned_data
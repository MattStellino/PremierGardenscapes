"""
Forms for the Premier Gardenscapes website.
Currently contains the contact form for customer inquiries.
"""

from django import forms


class ContactForm(forms.Form):
    """
    Contact form for customer inquiries.
    
    Fields:
        name: Customer's full name (required)
        email: Customer's email address (required)
        message: Customer's message/inquiry (required)
    """
    
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your full name',
            'aria-label': 'Full name'
        }),
        help_text='Please enter your full name'
    )
    
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'your.email@example.com',
            'aria-label': 'Email address'
        }),
        help_text='Please enter a valid email address'
    )
    
    message = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Tell us about your landscaping needs...',
            'aria-label': 'Your message'
        }),
        help_text='Please describe your landscaping project or inquiry'
    )
    
    def clean_name(self):
        """Clean and validate the name field."""
        name = self.cleaned_data.get('name')
        if name and len(name.strip()) < 2:
            raise forms.ValidationError('Name must be at least 2 characters long.')
        return name.strip()
    
    def clean_message(self):
        """Clean and validate the message field."""
        message = self.cleaned_data.get('message')
        if message and len(message.strip()) < 10:
            raise forms.ValidationError('Message must be at least 10 characters long.')
        return message.strip()

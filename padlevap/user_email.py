# your_app/email.py
from djoser import email
#import email


class PasswordResetEmail(email.PasswordResetEmail):
    template_name = 'email/password_reset_email.html'

    def get_context_data(self):
        context = super().get_context_data()
        # Add custom context variables
        context['site_name'] = "padlev.com"
        return context


class UsernameResetEmail(email.UsernameResetEmail):
    template_name = 'email/username_reset_email.html'
    
    def get_context_data(self):
        context = super().get_context_data()
        # Add custom context variables
        context['site_name'] = "padlev.com"
        #context['support_email'] = "support@example.com"
        return context


class PasswordChangedConfirmation(email.PasswordChangedConfirmationEmail):
    template_name = 'email/password_changed_confirmation.html'
    
    def get_context_data(self):
        context = super().get_context_data()
        # Add custom context variables
        context['site_name'] = "padlev.com"
        return context



class UsernameChangedConfirmation(email.UsernameChangedConfirmationEmail):
    template_name = 'email/username_changed_confirmation.html'
    
    def get_context_data(self):
        context = super().get_context_data()
        context['site_name'] = "padlev.com"
        return context


       
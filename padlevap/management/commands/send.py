from django.core.management.base import BaseCommand
from django.core.mail import send_mail

class Command(BaseCommand):
    help = "Send follow-up email after 1 day"

    def handle(self, *args, **kwargs):
        subject = 'Thanks for joining Padlev!'
        message = 'Hey there! 👋\n\nThanks for joining Padlev. We hope you’re enjoying your padel journey with us.\n\nFeel free to explore more on our site or contact us for any help.\n\nCheers,\nThe Padlev Team'
        from_email = 'Padlev <contact@padlev.com>'
        recipient_email = 'cheriet.imc@gmail.com'

        send_mail(subject, message, from_email, [recipient_email])

        self.stdout.write(self.style.SUCCESS("Follow-up email sent successfully."))

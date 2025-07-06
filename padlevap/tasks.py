from celery import shared_task
from django.core.mail import send_mail
from django.template.loader import render_to_string

@shared_task
def send_second_email(data, language):
    # Determine the subject and HTML template for the second email
    if language == 'en':
        subject = 'Your Free Book is Here – Grab Your Copy Now!'
        html_message = render_to_string('padlevap/en.html', data)
    elif language == 'fr':
        subject = 'Rappel: Votre livre gratuit est ici – Téléchargez votre exemplaire maintenant !'
        html_message = render_to_string('padlevap/fr.html', data)
    elif language == 'ar':
        subject = 'تذكير: كتابك المجاني هنا – احصل على نسختك الآن!'
        html_message = render_to_string('padlevap/ar.html', data)
    elif language == 'de':
        subject = 'Erinnerung: Ihr kostenloses Buch ist da – Holen Sie sich jetzt Ihr Exemplar!'
        html_message = render_to_string('padlevap/de.html', data)
    elif language == 'es':
        subject = 'Recordatorio: Tu libro gratis está aquí – ¡Consigue tu copia ahora!'
        html_message = render_to_string('padlevap/es.html', data)
    elif language == 'it':
        subject = 'Promemoria: Il tuo libro gratuito è qui – Scarica la tua copia ora!'
        html_message = render_to_string('padlevap/it.html', data)
    elif language == 'nl':
        subject = 'Herinnering: Je gratis boek is hier – Download nu je exemplaar!'
        html_message = render_to_string('padlevap/nl.html', data)
    elif language == 'pt':
        subject = 'Lembrete: Seu Livro Grátis Está Aqui – Baixe Sua Cópia Agora!'
        html_message = render_to_string('padlevap/pt.html', data)
    elif language == 'ru':
        subject = 'Напоминание: Ваша бесплатная книга здесь – получите свою копию прямо сейчас!'
        html_message = render_to_string('padlevap/ru.html', data)
    else:
        subject = 'Påminnelse: Din gratis bok är här – hämta din kopia nu!'
        html_message = render_to_string('padlevap/sv.html', data)

    # Send the second email
    plain_message = html_message
    from_email = 'Padlev <support@azguer.com>'
    to = data['email']

    send_mail(subject, plain_message, from_email, [to], html_message=html_message)






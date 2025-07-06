import logging
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
 
def send_email1(email, language, name):
    data = {
        'email': email,
        'language': language,
        'name':name
    }
    if language == 'en':
        subject = 'The Secret Shot Pros Use to Outsmart Opponents (Try It Now!)'
        html_message = render_to_string('email1/en.html', data)
    elif language == 'fr':
        subject = 'Le coup secret que les pros utilisent pour déjouer leurs adv'
        html_message = render_to_string('email1/fr.html', data)
    elif language == 'ar':
        subject = 'الضربة السرية التي يستخدمها المحترفون للتغلب على الخصوم'
        html_message = render_to_string('email1/ar.html', data)
    elif language == 'de':
        subject = 'Der geheime Schlag, mit dem Profis ihre Gegner überlisten'
        html_message = render_to_string('email1/de.html', data)
    elif language == 'es':
        subject = 'Golpe secreto de pros para vencer rivales (¡Pruébalo ya!)'
        html_message = render_to_string('email1/es.html', data)
    elif language == 'it':
        subject = 'Colpo segreto dei pro per battere gli avversari (Provalo!)'
        html_message = render_to_string('email1/it.html', data)
    elif language == 'nl':
        subject = 'Geheime slag van pro’s om tegenstanders te slim af te zijn!'
        html_message = render_to_string('email1/nl.html', data)
    elif language == 'pt':
        subject = 'Golpe secreto dos profissionais para vencer os adversários!'
        html_message = render_to_string('email1/pt.html', data)
    elif language == 'ru':
        subject = 'Секретный удар профи, чтобы обыграть соперников!'
        html_message = render_to_string('email1/ru.html', data)
    else:
        subject = 'Proffsets hemliga slag för att överlista motståndare!'
        html_message = render_to_string('email1/sv.html', data)
    plain_message = strip_tags(html_message)  # Changed from plain_message = html_message
    from_email = 'Padlev <contact@padlev.com>'
    
    # Changed 'to' to 'email' since that's your parameter
    send_mail(
        subject,
        plain_message,
        from_email,
        [email],  # This was [to] which wasn't defined
        html_message=html_message,
        fail_silently=False
    )
    return "ok"












#2 eme email




def send_email2(email, language):
    data = {
        'email': email,
        'language': language
    }
    if language == 'en':
        subject = 'Avoid Muscle Tears with This Simple Pre-Game Routine'
        html_message = render_to_string('email2/en.html', data)
    elif language == 'fr':
        subject = 'Évitez les blessures musculaires avec cette routine simple'
        html_message = render_to_string('email2/fr.html', data)
    elif language == 'ar':
        subject = 'تجنب تمزق العضلات مع هذا الروتين البسيط قبل المباراة'
        html_message = render_to_string('email2/ar.html', data)
    elif language == 'de':
        subject = 'r!Vermeide Muskelrisse mit dieser einfachen Vor-Spiel-Routine'
        html_message = render_to_string('email2/de.html', data)
    elif language == 'es':
        subject = 'Evita lesiones con esta rutina previa al juego'
        html_message = render_to_string('email2/es.html', data)
    elif language == 'it':
        subject = 'Evita strappi muscolari con questa routine pre-partita'
        html_message = render_to_string('email2/it.html', data)
    elif language == 'nl':
        subject = 'Voorkom spierscheuren met deze eenvoudige warming-up'
        html_message = render_to_string('email2/nl.html', data)
    elif language == 'pt':
        subject = 'Evite lesões musculares com esta rotina pré-jogo simples'
        html_message = render_to_string('email2/pt.html', data)
    elif language == 'ru':
        subject = 'Избегайте травм мышц простой предматчевой разминкой'
        html_message = render_to_string('email2/ru.html', data)
    else:
        subject = 'Undvik muskelskador med denna enkla förmatchrutin'
        html_message = render_to_string('email2/sv.html', data)
    plain_message = strip_tags(html_message)  # Changed from plain_message = html_message
    from_email = 'Padlev <contact@padlev.com>'
    
    # Changed 'to' to 'email' since that's your parameter
    send_mail(
        subject,
        plain_message,
        from_email,
        [email],  # This was [to] which wasn't defined
        html_message=html_message,
        fail_silently=False
    )
    return "ok"








#3 eme email 



def send_email3(email, language):
    data = {
        'email': email,
        'language': language
    }
    if language == 'en':
        subject = 'Psych Out Your Rival with This Pro Trick'
        html_message = render_to_string('email3/en.html', data)
    elif language == 'fr':
        subject = 'Déstabilisez votre adversaire avec cette astuce de pro'
        html_message = render_to_string('email3/fr.html', data)
    elif language == 'ar':
        subject = 'افقد خصمك تركيزه بهذه الخدعة الاحترافية'
        html_message = render_to_string('email3/ar.html', data)
    elif language == 'de':
        subject = 'Bring deinen Gegner mit diesem Profi-Trick aus dem Konzept'
        html_message = render_to_string('email3/de.html', data)
    elif language == 'es':
        subject = 'Descoloca a tu rival con este truco profesional'
        html_message = render_to_string('email3/es.html', data)
    elif language == 'it':
        subject = 'Sconvolgi il tuo avversario con un trucco da pro'
        html_message = render_to_string('email3/it.html', data)
    elif language == 'nl':
        subject = 'Verwarring bij je tegenstander met deze pro-truc'
        html_message = render_to_string('email3/nl.html', data)
    elif language == 'pt':
        subject = 'Desestabilize seu rival com este truque de profissional'
        html_message = render_to_string('email3/pt.html', data)
    elif language == 'ru':
        subject = 'Выведи соперника из равновесия этим профессиональным приёмом'
        html_message = render_to_string('email3/ru.html', data)
    else:
        subject = 'Överraska din rival med detta proffs-trick'
        html_message = render_to_string('email3/sv.html', data)
    plain_message = strip_tags(html_message)  # Changed from plain_message = html_message
    from_email = 'Padlev <contact@padlev.com>'
    
    # Changed 'to' to 'email' since that's your parameter
    send_mail(
        subject,
        plain_message,
        from_email,
        [email],  # This was [to] which wasn't defined
        html_message=html_message,
        fail_silently=False
    )
    return "ok"



#4 eme email 


def send_email4(email, language):
    data = {
        'email': email,
        'language': language
    }
    if language == 'en':
        subject = '70% of Points Are Decided at the Net, Are You Ready?'
        html_message = render_to_string('email4/en.html', data)
    elif language == 'fr':
        subject = '70 % des points se décident au filet, êtes-vous prêt ?'
        html_message = render_to_string('email4/fr.html', data)
    elif language == 'ar':
        subject = '٧٠٪ من النقاط تُحسم عند الشبكة، هل أنت مستعد؟'
        html_message = render_to_string('email4/ar.html', data)
    elif language == 'de':
        subject = '70 % der Punkte werden am Netz entschieden – bist du bereit?'
        html_message = render_to_string('email4/de.html', data)
    elif language == 'es':
        subject = 'El 70 % de los puntos se deciden en la red, ¿estás listo?'
        html_message = render_to_string('email4/es.html', data)
    elif language == 'it':
        subject = 'Il tuo libro gratuito è qui – Scarica la tua copia ora!'
        html_message = render_to_string('email4/it.html', data)
    elif language == 'nl':
        subject = 'Il 70% dei punti si decidono a rete, sei pronto?'
        html_message = render_to_string('email4/nl.html', data)
    elif language == 'pt':
        subject = '70% dos pontos são decididos na rede, você está pronto?'
        html_message = render_to_string('email4/pt.html', data)
    elif language == 'ru':
        subject = '70% очков решаются у сетки, ты готов?'
        html_message = render_to_string('email4/ru.html', data)
    else:
        subject = '70 % av poängen avgörs vid nätet, är du redo?'
        html_message = render_to_string('email4/sv.html', data)
    plain_message = strip_tags(html_message)  # Changed from plain_message = html_message
    from_email = 'Padlev <contact@padlev.com>'
    
    # Changed 'to' to 'email' since that's your parameter
    send_mail(
        subject,
        plain_message,
        from_email,
        [email],  # This was [to] which wasn't defined
        html_message=html_message,
        fail_silently=False
    )
    return "ok"
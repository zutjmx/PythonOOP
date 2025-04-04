import os
import resend

api_key = os.getenv('API_KEY_RESEND')

print(f'API_KEY_RESEND: {api_key}')

resend.api_key = api_key

r = resend.Emails.send({
  "from": "onboarding@resend.dev",
  "to": "zutjmx@gmail.com",
  "subject": "Hello World",
  "html": "<p>Congrats on sending your <strong>first email</strong>!</p>"
})
print('Mensaje enviado, checa tu mail.')

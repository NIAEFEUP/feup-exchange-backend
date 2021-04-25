from utils.mail import send_mail_to_students

if __name__ == '__main__':
  receivers = [
    "kikojpgoncalves@gmail.com",
  ]
  subject = "subject"
  body = """Boa tarde a todos,
O processo de escolha de horarios...
Assim sendo, criámos o feup-exchange...
Desejamos a todos um bom semestre, 
NIAEFEUP.
"""
  
  send_mail_to_students(
      subject,
      body,
      receivers
  )
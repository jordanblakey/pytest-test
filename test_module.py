def test_ehlo(smtp_connection):
  # print(smtp_connection.ehlo())
  response, msg = smtp_connection.ehlo()
  # print('response:', response, 'msg:', msg)
  assert response == 250


def test_noop(smtp_connection):
  response, msg = smtp_connection.noop()
  assert response == 250

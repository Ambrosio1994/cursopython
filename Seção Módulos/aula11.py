import secrets
import string

gerador = secrets.token_urlsafe(8)
print(gerador)
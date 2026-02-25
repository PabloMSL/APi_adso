from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from firebase_admin import auth
import firebase_admin

class FirebaseAuthentication(BaseAuthentication):
    """
    Lerr el token JWT del encabezado. Lo va a validar con firebase y va a extraer e UID del usuario
    """
    def authenticate(self, request):
       # Extraemos el token
       auth_header = request.META.get('HTTP_AUTHORIZATION') or request.headers.get('Authorization')
       if not auth_header:
           return None #Si no hay token
       
       # El token viene "Bearer <<token>>"

       partes = auth_header.split()

       if len(partes) != 2 or partes[0].lower() != 'bearer':
           return None
       
       token = partes[1]

       try:
            # Le pido a firebase que valide la firma del Token
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token.get('uid')
            # Usuario
            class FirebaseUser:
               is_authenticated = True
               def __init__(self, uid):
                   self.uid = uid
            
            return(FirebaseUser(uid), decoded_token)
       except Exception as e:
           raise AuthenticationFailed(f"Token no es valido o esta expirado: {str(e)}")
       
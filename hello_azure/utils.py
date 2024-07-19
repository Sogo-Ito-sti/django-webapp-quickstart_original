from jose import jwt

def decode_id_token(id_token):
    decoded_token = jwt.decode(id_token, options={"verify_signature": False})
    user_id = decoded_token.get('sub')  # 'sub' はユーザーの識別子
    return user_id

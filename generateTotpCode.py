import hmac
import hashlib
import base64
import time
import math

OTP_DIGITS = 10

def main():
  while True:
    print("Press 0 to enter the secret as plain text")
    print("Press 1 to enter the string as base32")
    print("Press Q to exit")
    choice = input()
    if(choice.upper() == "Q"):
      break
    elif(choice == "0"):
      otpCode = generateOTPFromTextSecret(input("Enter the plain text shared secret: "))
      print(otpCode)
    elif(choice == "1"):
      otpCode = generateOTPFromBase32Secret(input("Enter the Base32 shared secret: "))
      print(otpCode)
    else:
      print("Choice not defined, try again.")

    

def generateOTPFromTextSecret(secret: str, digits: int = None):
  if(digits == None):
    digits = OTP_DIGITS
  secret = secret.encode("ascii")
  counter = math.floor(time.time()/30).to_bytes(8, "big")
  otpCode = generateOTP(secret, counter, digits)
  return ("{:0" + str(digits) +"d}").format(otpCode)

def generateOTPFromBase32Secret(secret: str, digits: int = None):
  if(digits == None):
    digits = OTP_DIGITS
  secret = base64.b32decode(secret.encode("ascii"))
  counter = math.floor(time.time()/30).to_bytes(8, "big")
  otpCode = generateOTP(secret, counter, digits)
  return ("{:0" + str(digits) +"d}").format(otpCode)

def generateOTP(secret: bytes, counter: bytes, digits: int):
  hashed = hmac.new(secret, counter, hashlib.sha512).digest()
  return truncate(hashed, digits)

def truncate(hashedBytes: bytes, digits: int):
  offset = int(hashedBytes[len(hashedBytes)-1]) & 15
  P = hashedBytes[offset:offset+4]
  ((P[0] << 1) >> 1)
  P = int.from_bytes(P, "big", signed=False)

  return P % pow(10, digits)


main()

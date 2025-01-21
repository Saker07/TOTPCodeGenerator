# TOTPCodeGenerator
Rudimentary python script to generate a Time-based One-Time Passwords according to RFC6238

The script was created for personal curiosity and to complete an online challenge.
You can change the number of digits returned by changing "OTP_DIGITS".
You can manually call generateOTPFromBase32Secret or generateOTPFromTextSecret to explicitly specify the counter and the number of digits.
The time is always based on Unix EPOCH

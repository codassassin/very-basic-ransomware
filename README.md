# very-basic-ransomware
This is a very basic ransomware created using Python

## requirements
```
requests~=2.24.0
cryptography~=2.9.2
```

## How to test the RANSOMWARE
* Edit the line 44, paste the testing directory in place of "The testing path".
* Edit the line 129, paste the Background pic directory.
* [ATTACKER] run the RSA_public_private_keys.py to generate 'public.pem' and 'private.pem'.
* [ATTACKER] send the 'RANSOMWARE.py' and 'public.pem' bundled together to the target machine in any way (bind the files along with any application).
* [TARGET] after the 'RANSOMWARE.py' gets executed all the mentioned extensions(in the code) files will be encrypted.
* [ATTACKER] Run the fernet key decryption file to decrypt the EMAIL_ME.txt(be on your desktop) file, this will give you a PUT_ME_ON_DESKTOP.txt file, once you put this on the desktop the ransomware will decrypt the encrypted files in that directory.


### Disclaimer !!

> This tool is only for testing and academic purposes and can only be used where strict consent has been given. Do not use it for
> illegal purposes! It is the end user’s responsibility to obey all applicable local, state and federal laws. Developers assume no
> liability and are not responsible for any misuse or damage caused by this tool and software in general.

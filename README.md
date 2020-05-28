# IronPortBlockEmail

### Cisco IronPort C380 Block E-mail Python Script. 


Hello everyone, my name is Willian Ferreira and I am here to share with the community a solution of a problem I faced at work.

This shell scripting queries a domain or sender in the blocked mailing list. he adds it to the list.

## Settings needed for this script to work.

* Need to create a private key on the server where the script will be.
* Create a user that will be used in the script.
* Add the public key that was generated on the IronPort C380 server as per tutorial https://somoit.net/ironport/ironport-automate-commands-scripts-from-linux

## Initial information

This scrpit was created to automate and block and unblock the Blacklist domain. It can be used as a service module.

In the example, it generates a list of all the domains contained in the list, lists a specific domain, adds and removes it from the list.

     ./blockEmail.py

## Variables

* HOST = "IP / HOSTNAME"
* LIST = "List that will be used. Ex: Blacklist"
* ironport = User who will connect to the CLI on ironport

## Final considerations.

Any doubt, I am available.

Feel free to send me a <b> poll request </b> to improve this code.
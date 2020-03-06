# hashcat-rule
I use hashcat (https://github.com/hashcat/hashcat/).
Rule are supposed to be mutual for john and hashcat or other.

> Rule for hashcat or john focused on password guessing based on medium wordlist input. ~4'700 rules

This is for basic coverage of passwords for normal people who only add 1 letter, 1 digits, 1 punctuation, 1 digits+punctuations, 2 digits+punctuations or a year (from 1900 to 2099) or some famous tricks (ex:p@$$w0rd) to their **master password**.

## Write your own rule

This is the only thing you need to write your rule : **https://hashcat.net/wiki/doku.php?id=rule_based_attack**

## Why another
> There is already some really good rules out there but best64 is too small and bigger ones are too big.
https://github.com/NotSoSecure/password_cracking_rules/ is good but does many random things and some result are silly.

> https://github.com/praetorian-code/Hob0Rules too small or too big

> https://github.com/NSAKEY/nsa-rules idem

I wanted a comprehensive rule based on people password rather than insane huge wordlist converted to rule. They are doing it in the other way to get a nice graph with '*look my rule is better because i got a better coverage rate !*'.


Moreover getting your hands dirty give you a better understanding of what you're doing.

## What i have done : 
(TO DO)
> input= password

passwordA

  ...(latin letters)

passwordz

password0

  ...(digits)

password0

password&

  ...(punctation)

password{

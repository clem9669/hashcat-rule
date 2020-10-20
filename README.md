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
> input= montagne

Exhaustive list of rules:

Action performed | Rule | Output 
-----|-------|-------
Lowercase all letters	 | l | 
Uppercase all letters	 | u | 
Capitalize the first letter and lower the rest | c | 
Lowercase first found character, uppercase the rest | C | 
Toggle the case of all characters in word | t | 
Swaps first two characters	 | k | 
Swaps last two characters | K | 
Duplicate entire word	 | d | 
Add 1 character at the end (printable) | Script python | 
Add 2 digits |Script python | 
Add 1 digit + 1 punctuation | Script python | 
Add 2 digits + 1 punctuation | Script python | 
Add 1 character at the end (printable) with capitalize the first letter | Script python | 
Add 2 digits with capitalize the first letter| Script python | 
Add 1 digit + 1 punctuation with capitalize the first letter| Script python | 
Add 2 digits + 1 punctuation with capitalize the first letter| Script python | 
Add 1 punctuation + 1 digit | Script python | 
Add 1 punctuation + 2 digits | Script python | 
Add 1 punctuation + 1 digit with capitalize the first letter| Script python | 
Add 1 punctuation + 2 digits with capitalize the first letter| Script python | 
Add all years from 1900 to 2099 | Script python | 
Add all years from 1900 to 2099 with capitalize the first letter|Script python | 
Add famous number | See rule | 
Add high frequency overwrite | See rule | 
Add high frequency prepend | See rule | 
Add high frequency overwrite at start | See rule | 
Leetify | See rule | 



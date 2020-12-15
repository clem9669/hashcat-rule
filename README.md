# hashcat-rule
I use hashcat (https://github.com/hashcat/hashcat/).
Rule are supposed to be mutual for john and hashcat or other.

> Rule for hashcat or john focused on password guessing based on medium wordlist input. ~~4'700 rules~~ => ~~11'659 rules~~ => ~~19'685 rules~~ => ~~26'132 rules~~ => 26'748 rules

This was for basic coverage of passwords for normal people who only add 1 letter, 1 digits, 1 punctuation, 1 digits+punctuations, 2 digits+punctuations or a year (from 1900 to 2099) or some famous tricks (ex:p@$$w0rd) to their **password**.

> Update: I have extented these rules to be more than just that.

The **Big** rule is :
* clem9669
* One Rule to Rule Them All
* InsidePro-*

The **medium** is only mine.

The **small** is only adding 1 character (start & end). 
It purpose is to be combined with others rules as: `-r clem9669_big.rule -r clem9669_small.rule`

```sh
$ wc -l clem9669*
 81966 clem9669_big.rule
 26748 clem9669_medium.rule
   191 clem9669_small.rule
   ```


## Write your own rule

This is the only thing you need to write your rule : **https://hashcat.net/wiki/doku.php?id=rule_based_attack**

See examples: https://github.com/hashcat/hashcat/tree/master/rules

## Why another
> There is already some really good rules out there but best64 is too small and bigger ones might be too big.
https://github.com/NotSoSecure/password_cracking_rules/ is good but does many random things

> https://github.com/praetorian-code/Hob0Rules too small or too big

> https://github.com/NSAKEY/nsa-rules idem

I wanted to make my own and i feel better using mine now. My rule are not random rules in clem9669_medium.


Moreover getting your hands dirty give you a better understanding of what you're doing.

## What i have done : 

> Input= password
> Please see a output example in **password_ruled.txt**

Almost exhaustive list of rules:

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
Various substitutions | s |
Title case | e |
Add 1  at the end (printable) | Script python | 
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
Add all years from 1900 to 2099 with ! at the end | Script python | 
Add all years from 1900 to 2099 with capitalize the first letter|Script python | 
Add all years from 1900 to 2099 with ! at the end with capitalize the first letter|Script python | 
Add all caps character at the end (printable) | See rule| 
Add all caps character + years from 1900 to 2099 | See rule| 
Add all caps character + years from 1900 to 2099 with ! at the end | See rule| 
Add all caps character + 1 digit | See rule| 
Add all caps character + 1 digit + 1 punctuation | See rule| 
Add famous number | See rule | 
Add famous number all caps| See rule | 
Add high frequency overwrite | See rule | 
Add high frequency prepend | See rule | 
Add high frequency overwrite at start | See rule | 
Leetify | See rule | 

AND MORE!!


<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/clem9669/hashcar-rule">
    <img src="https://www.fai.org/sites/default/files/styles/basic_page_highlighted_mlarge/public/isc/rules.jpeg" alt="Logo" width="400" height="200">
  </a>

  <h3 align="center">Hashcat-rules</h3>

  <p align="center">
    Crack people password with rules (hashcat & john)
  </p>

> check out my wordlist project at: https://github.com/clem9669/wordlists

## Introduction
I use hashcat (https://github.com/hashcat/hashcat/).
Rule are supposed to be mutual for john and hashcat or other.

> 3 rules exists to adapt hashing algorithm speed. Large for fast hash algorithm as md4&md5. Small for slow hash algorithm as bcrypt.

This was for basic coverage of passwords for normal people who only add 1 letter, 1 digits, 1 punctuation, 1 digits+punctuations, 2 digits+punctuations or a year (from 1900 to 2099) or some famous tricks (ex:p@$$w0rd) to their **password**.

> Update: I have extented these rules to be more than just that.

The **Big** rule is :
* clem9669 medium list
* mp64 (https://hashcat.net/wiki/doku.php?id=maskprocessor)
* One Rule to Rule Them All
* InsidePro-PasswordsPro
* InsidePro-HashManager

The **medium** is only mine.

The **small** is only adding 1 character (start & end) with toogle cases. 
It purpose is to be combined with others rules as: `-r clem9669_big.rule -r clem9669_small.rule` or to be used as is with low rate cracking algorithm.

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

> There is already some really good rules out there but best64 is too small and bigger ones might be too big with too many random thing for a certain language as french.


* https://github.com/NotSoSecure/password_cracking_rules, is good but does many random things

* https://github.com/praetorian-code/Hob0Rules, too many random rules

* https://github.com/NSAKEY/nsa-rules, idem

I wanted to make my own and i feel better using mine now. My rule are not random rules in clem9669_medium.


Moreover getting your hands dirty give you a better understanding of what you're doing.

## What i have done : 

> Input= password
> Please see a output example for [clem9669_large.rule](https://github.com/clem9669/hashcat-rule/blob/master/clem9669_large.rule) in [**password_ruled.txt**](https://github.com/clem9669/hashcat-rule/blob/master/password_ruled.txt) !!

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


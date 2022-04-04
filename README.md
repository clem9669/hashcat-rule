<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/clem9669/hashcar-rule">
    <img src="https://www.fai.org/sites/default/files/styles/basic_page_highlighted_mlarge/public/isc/rules.jpeg" alt="Logo" width="400" height="200">
  </a>

  <h3 align="center">Hashcat-rules</h3>

  <p align="center">
    Crack people's passwords with rules (hashcat & john)
  </p>

> Check out my wordlist project at: https://github.com/clem9669/wordlists

## Introduction
I use hashcat (https://github.com/hashcat/hashcat/).
Rule are supposed to be compatible for john and hashcat or others.

> 3 rules exists to adapt to hashing algorithm speed. Large for fast hash algorithms like MD5/NTLM/MySQL3. Small for slow hash algorithms like bcrypt.

This was for basic coverage of passwords for non-educated people who only add 1 letter, 1 digit, 1 punctuation, 1 digit+punctuation, 2 digits+punctuation or a year or some other famous tricks *(ex: p@$$w0rd)* to their **password**.

> 📣 Update: I have extented these rules to be more than just that. 📣


## Running rules

I have removed casing in Large & Medium. Please run as: `-r toggle-case.rule -r clem9669_big.rule`

The **Big** rule is :
* clem9669 medium list
* mp64 (https://hashcat.net/wiki/doku.php?id=maskprocessor)
* One Rule to Rule Them All
* InsidePro-PasswordsPro
* InsidePro-HashManager
* Fordy50K

The **medium** is mine.

The **small** is only adding 1 character (start & end) with toogle cases. 
Its purpose is to be combined with others rules as: `-r clem9669_big.rule -r clem9669_small.rule` or to be used as is with low rate cracking algorithms.

### Rules size

```sh
$ wc -l clem9669*
 3549903 clem9669_big.rule (50M)
  170474 clem9669_medium.rule (3.3M)
     374 clem9669_small.rule (1.7K)
```

## Write your own rules

This is the only thing you need to write your rules : **https://hashcat.net/wiki/doku.php?id=rule_based_attack**

I recommend using [clem9669_small](https://github.com/clem9669/hashcat-rule/blob/master/clem9669_small.rule) as a reference to start understanding how to write rules.

## Why another

> There are already some really good rules out there but best64 is too small and bigger ones might be too big with too many random things when targeting a certain language like french.


* https://github.com/NotSoSecure/password_cracking_rules, is good but does many random things

* https://github.com/praetorian-code/Hob0Rules, too many random rules

* https://github.com/NSAKEY/nsa-rules, idem

I wanted to make my own and I feel better using mine now. My rules are not random rules in clem9669_medium.


Moreover getting your hands dirty gives you a better understanding of what you're doing.

## Saving which rules matched


This becomes handy especially in combination with the rules generator but also for statistical analysis of your rule sets.

To save any rule that generated a matched password, use these switches:

`--debug-mode=4 --debug-file=matched.rule`


This will save the matched rule on every match, so the resulting rule file might contain many duplicate rules.

> At high rates of cracking per second, this may slow down cracking a little bit. 
> At lower rates of cracking per second, the impact is probably negligible.

## Testing and ouputing rules

With hashcat we can debug our rules easily. This means we can verify that the rule we wrote actually does what we want it to do. 
All you need to use is the **--stdout** switch and omit the hashlist. 

`hashcat -r clem9669_large.rule --stdout password`

See sample [password_ruled.txt](https://github.com/clem9669/hashcat-rule/blob/master/password_ruled.txt)

## What I have done : 

> Input= password
> Please see a output example for [clem9669_large.rule](https://github.com/clem9669/hashcat-rule/blob/master/clem9669_large.rule) in [**password_ruled.txt**](https://github.com/clem9669/hashcat-rule/blob/master/password_ruled.txt) !!

Almost exhaustive list of rules:

Action performed | Rule | Output 
-----|-------|-------
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
Preappend top 100 prenoms | See rule | 
Preappend top adverbs | See rule | 
Preappend top verbs | See rule | 
Preappend top adjectives | See rule | 
Preappend top 100 prenoms with capitalize the first letter| See rule | 
Preappend top adverbs with capitalize the first letter| See rule | 
Preappend top verbs with capitalize the first letter| See rule | 
Preappend top adjectives with capitalize the first letter| See rule | 

AND MORE!!

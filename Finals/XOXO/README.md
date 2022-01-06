# XOXO

## Challenge Description 

Did you know: if a^b=c then a^c=b

## Challenge file

[Primary link](https://gitlab.com/teambi0s/inctf-junior/finals/2021/-/blob/main/Forensics/xoxo/Handout/xoxo.png)

## Short write up

Xoring the given png with magic numbers of png (`89 50 4E 47 0D 0A 1A 0A`) will give the key as `eAsy-x0r`

With  that key, we can xor the rest of the png, which will give the flag

## Flag 

inctfj{x0riNg_iS_fUn!!}

## Author 
[rayst4rk](https://twitter.com/rayst4rk)

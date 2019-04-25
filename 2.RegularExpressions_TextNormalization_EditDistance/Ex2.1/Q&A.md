#####Write regular expressions for the following languages.
```
1.the set of all alphabetic strings;
2.the set of all lower case alphabetic strings ending in a b;
3.the set of all strings from the alphabetic a,b such that 
each a is immediately preceded by and immediately followed by a b
```

```
1./[a-zA-Z]+/
2./[a-z]*b\b/
3./\bb+(b|ab)*\b/
```

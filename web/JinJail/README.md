# jinjail
**Category:** Web
**Difficulty:** Easy
**Author:** downgrade

## Description

I've looked all over the internet for payloads or techniques to bypass my SSTI filter, but none would work! Surely this is secure?

## Distribution

jinjail-dist.zip

## Solution

Create strings without quotes by creating a dict with a key of the desired string, converting the dict to a list, and taking the first element of the list: `(dict(__globals__=x)|list)[0]` == `"__globals__"`. Other tricks also required, but this is the main idea. Full payload in `healthcheck/healthcheck.py` 

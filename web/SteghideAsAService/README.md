# steghide-as-a-service
**Category:** Web
**Difficulty:** Medium-Hard
**Author:** downgrade

## Description

As has long been demonstrated by CTF, only the most 1337 are capable of running steghide. To help bridge this immense skill gap, I created a web based tool for easy embedding of hidden messages.

## Distribution

SaaS-dist.zip

## Solution

LFI through a small chain of exploits. The randomly generated guest username is appended to the uploaded filename, with an underscore in between ('x.jpeg\_guest123'). The session cookie is not actually verified until after the file upload, so we can sign our own JWT with the file we're uploading. There is a simple filter in place to stop directory traversal (removal of "..") in the JWT header, but due to os.path.join(), this can be bypassed using the absolute path to the uploaded file. Because of the underscore, we need to directory traverse to a directory that has an underscore in its name. One such directory is `/proc/self/map_files`. So our uploaded filename will be `..././..././..././..././..././proc/self/map`, and our JWT username will be `files/../../../app/flag.txt`. After filtering and joining, the final path becomes `output/../../../../../proc/self/map_files/../../../app/flag.txt`, which is sent to the attacker.

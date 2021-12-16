# difference-checker
**Category:** Web
**Difficulty:** Easy
**Author:** downgrade

## Description

It's important two know what differences exist, so I created a simple tool to check the difference between two websites!

## Distribution

difference-check-dist.zip

## Solution

The ssrf filter checks all of the links first, and then sends a request to each link. Simply create a server that alternates between an innocent response and a redirect to localhost:1337/flag

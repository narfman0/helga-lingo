helga-lingo
======================

Define words from urbandictionary.com

Usage
-----

``!lingo <term>``

This queries urbandictionary for the given term

Example:
    !lingo dig

Returns:
    A word to use when you're insulting someone. Like a "burn" or a "blast". An
    insult. A dig isn't usually meant seriously. It's normally used in a joking
    manner with a hint of truth. :)

``!lingo <term> <index>``

When a term has multiple definitions, one may retrieve a consecutive definition
by incrementing index. It implicitly starts at 0, so not including it is like
getting the 0th definition.

Example:
    !lingo dig 2

Returns (the third definition content):
    v.
    1. To perceive and comprehend the nature and significane of; grasp; gather.
    "Ya dig? Yeah I can dig it"
    etc.

``!lingo -d <term>``

Execute regular lingo query, but return debug results as well

Methodology
-----------

Uses the official urbandictionary api, parsing the json response, and returning
the definition according to the index the user provides. By default, this is the
first, or 0th, index.

An example API call for the term 'api' would be:
    api.urbandictionary.com/v0/define?term=api

License
-------

Copyright (c) 2014 Jon Robison

See included LICENSE for licensing information

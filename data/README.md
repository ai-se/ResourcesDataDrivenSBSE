# How to "Make" the site

What a surprise:

    make site

To preview the content:

    brew install grip
    # or sudo apt-get install grip
    grip ../var/pubs.md

The content is written to ../var. 

- Note that that directory .gitignored (so many people can check out this repo and
explore content). 
- If that content looks good to you, send a pull request and the site organziers will run your update and place it
on-line directory ../doc.

**IMPORTANT**: Pretty please, **DO NOT DO MOVE**  content into ../doc  yourself (that way, version control madeness lies).

- Send us a pull request and we'll do it.
- Thanks!

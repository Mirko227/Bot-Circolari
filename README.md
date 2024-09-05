# Bot-Circolari
Telegram bot circolari ITIS Fermi
I developed a Python script that performs web scraping of circulars from the website of the Enrico Fermi Institute in Rome. The script formats the description of the circulars, links to any attachments, and the text of the circulars themselves, saving them in a .txt file to keep track of the circulars that have already been sent and to avoid losing the list in case of a script restart. This script ran continuously on a Raspberry Pi and was integrated with a Telegram bot, allowing students and families to quickly read and stay updated on the new circulars published on the site.

To avoid computational cost O(n) with very large n, the .txt file is automatically cleared after a certain number of circulars. Since the website displays only a limited number of circulars at a time, it is sufficient to keep track of only the most recent circulars.

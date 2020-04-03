# It's a Secret to Everybody

<img src="https://objects-us-east-1.dream.io/secrettoeverybody/images/secret.png" width="50%" />

## Description

<img src="https://upload.wikimedia.org/wikipedia/commons/c/c2/Danc-01.jpg" width="33%" />

Sir Arthur Conan Doyle wrote "The Adventure of the Dancing Men" in 1905. In it, Holmes receives a request for help from a man whose wife has been receiving strange messages. The notes appear to contain only drawings of dancing stick figures, but leave her inexplicably terrified.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/Dancing_men.svg/692px-Dancing_men.svg.png" width="50%" />

Holmes realizes that the stick men are actually a code. Each different figure corresponds to one letter of the alphabet and the flags mark the boundaries between words. Holmes breaks the code and learns the truth...which you'll have to learn for yourself by reading the story

The Dancing Men are an example of a **substitution cipher**: one of the simplest techniques for encoding secret messages. In this scheme, each letter in the **plaintext message** is mapped to a different letter of the alphabet to yield the **ciphertext message**. Knowing the substitutions allows the encryption to be reversed.

For example,the coded message `GHHGDB GH EGJM` could be deciphered as `ATTACK AT DAWN` by substituting

- A for G
- T for H
- C for D
- K for B
- D for E
- W for J
- M for N.

Although substitution ciphers are easy to implement they are insecure, because they’re vulnerable to **frequency analysis attack**.

The letters of English words are not randomly distributed: *e* is the most common (about 13% of occurrences), followed by *t* (9%) and then *a* (8%). Letters *q* and *z* each account for less than 1% of occurrences in common English text.

Therefore, given a large body of text that’s been encoded using a substitution cipher, the most frequently occurring letter is likely to be *e*, with the second most frequently occurring *t*, and so forth. Even when the correspondence between encrypted and decrypted letter frequencies is not exact, frequency analysis often yields enough information about the message to make decryption possible.

In this project, your mission is to use frequency analysis to decipher a message that I’ve encoded using a substitution cipher. Use frequency analysis to determine the letter frequencies in the enciphered text. Then, using a table of standard English letter frequencies, decrypt the ciphertext to produce the plaintext output.

## Getting the Input File

The enciphered message is in the file `cipher.txt` posted to Canvas. It contains the opening text of a famous work of literature. The punctuation, spaces, and capitalization of the text have been left intact and both capital and lowercase letters have been encrypted using the same substitutions.

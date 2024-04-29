
## ASCII VS UNICODE

ASCII ( American Standard Code for Information Interchange ) and Unicode are character encoding standards used in computing to represent text as numbers. Both ASCII and Unicode assign a unique numerical value to each character in a character set, allowing computers to store, process, and transmit textual data . 

| Eencoding Standard | Description |
| --- | --- | 
| ASCII | ASCII ( American Standard Code for Information Interchange ).<br>ASCII is one of the earliest character encoding standards, developed in the 1960s.<br>It originally used 7 bits to represent characters, allowing for 128 different characters , including : letters, digits, punctuation marks, and control characters . <br>ASCII encoding primarily covers characters used in the English language, but it lacks support for characters from other languages and special symbols.<br>Extended ASCII ( 8 bits ASCII ) was later introduced to support additional characters, with different variations used in different regions of the world. | 
| UNICODE | Unicode is a more comprehensive character encoding standard designed to support characters from all writing systems in the world.<br>It uses a variable-length encoding scheme, typically UTF-8, UTF-16, UTF-32 to represent characters using 8,16,32 respectively.<br>Unicode assigns a unique numerical code point to each character, including ; letters, digits, symbols, emojis, and characters from various languages and scripts.<br>Unicode includes ASCII as a subset, with the first 128 code points identical to ASCII.<br>Unicode allowed for multilingual text processing, enabling software to handle text in multiple languages seamlessly. |

----

Encoding and decoding are processes used in computer science and information technology to represent and interpret data in various formats. 

Here's what each term means : 

| Format | Descriptions | 
| --- | --- | 
| Encoding | Encoding is the process of converting data from one form or representation to another.<br>In the context of character encoding, encoding refers to converting textual data (characters) into a specific format that can be stored, transmitted, or processed by computers.<br>For example, when you type text on a keyboard, the characters you input are encoded into binary data (0s and 1s) using a character encoding scheme such as ASCII, Unicode, or UTF-8.<br>Encoding can also refer to the process of converting data into a specific format for transmission over a network, storage on disk, or encryption for security purposes. |
| Decoding | Decoding is the process of interpreting encoded data and converting it back into its original form or representation.<br>In the context of character encoding, decoding involves converting binary data (0s and 1s) back into textual characters using the appropriate character encoding scheme.<br>For example, when a computer receives binary data over a network, it decodes the data using the agreed-upon encoding scheme to reconstruct the original text.<br>Decoding can also refer to the process of interpreting encoded data in other contexts, such as decoding compressed files, decoding multimedia data (e.g., audio, video), or decoding encrypted data. |

---
In summary, encoding involves converting data into a specific format, while decoding involves interpreting encoded data and converting it back into its original form. These processes are essential for communication, data storage, data processing, and various other tasks in computing .

---

# COMP3028-Computer-Security-Coursework-3

## Task 2 answer

Question: How MFA improves security compared to a single password, and what threats it mitigates.

- Multi-factor authentication (MFA) secures account by requesting the user to provide two or more independent pieces of evidence before granting access to user's account, system or service. A single password relies on something the user knows which is the password user has set. Thus, MFA provides increased security by combining single password with other elements such as something the user has (smartphone or security token) or something the user is (fingerprint or facial recognition).
- This multi-layered approach reduces the possibility of unauthorised access by a considerable amount. If a password is hacked or taken through attacks like phishing, the intruder would have to cross at least another stand-alone security layer. For example, if an intruder acquires user's password, the intruder cannot access user's account without having access to user's phone at the same time for a one-time code or user's fingerprint for biometric authentication.
- Threats MFA can mitigate are:
  - Brute-force attacks: Automated guessing of passwords is defeated because a password alone is insufficient to provide access.
  - Password reuse attacks: MFA compensates for the use of reused passwords across sites because second factors specific to accounts are employed. Password management.
  - Phishing attacks: If the user is fooled into divulging a password, the attacker is still required to have the second factor, making phishing much less efficient.
  - Replay attacks: Time-limited use, one-time codes or authentication tokens prevent attackers from reusing captured credentials.
  - Credential stuffing: Attackers using stolen credentials from a single breach to authenticate to other accounts are barred without the second factor.
- Therefore, MFA makes unauthorised access infinitely harder, even to attackers who already have jumped through the password hurdles. It is a crucial safeguard against most of today's password-based authentication focused cyber attacks.

## Task 3 
In our attempt at decrypting the password, we used three types of password cracking tools:
### 1. Dictionary Attack
This form attack uses a 'dictionary', a document that stores some of the most popular passwords used by people. It takes the hashed password and compares it with each password in the document. This is very effective against weak passwords or those based on real words or common patterns.

Some examples of passwords and time taken to crack:

| password | time taken (seconds) |
| --- | --- |
| password | 0.21 |
| abc123 | 2.99 |
| garfield | 91.35 |
| qwerty | 1.07 |

One way of preventing a dictionary attack could be to stay away from using common nouns, names and such. 

### 2. Intelligence Guess Attack 
This form of attack makes use of the user's details that may have been leaked in some way or accessed by the hacker. This is very dangerous and especially effective if the hacker knowns the user personally and has knows their personal data.

In our example, we simulated the user's info: 
```python
name : 'carmel'
birthyear : 2004
pet: 'beans'
```

Some examples of passwords and time taken to crack:

| password | time taken (seconds) |
| --- | --- |
| carmel | 0.21 |
| carmel2004 | 0.86 |
| carmel123 | 0.43 |
| beans | 1.07 |
| beans123 | 1.28 |

As you can see, the time taken to crack the password is very fast when the hacker knows the user's personal information. A good way to avoid it is to simply not use your details or add random phrases and characters to it (i.e. `beansAppleRabbit12`)

### 3. Brute Force Attack
This form of attack attempts to use every possible combination of characters (letters, numbers and symbols) up to a certain length. While this can eventually crack the password, it becomes computationally expensive especially if the password is exceptionally long and contains a mixture of characters.

Some examples of passwords and time taken to crack:

| password | time taken (seconds) |
| --- | --- |
| a | 0.21 |
| z | 5.55 |
| aa | 5.79 |
| az | 11.17 |
| abc | 156.86 |
| A# | 972.43 |

As you can see from the table above, there is a huge jump in the time taken to crack a two-letter password versus a three-letter password and an even larger jump in time taken when adding a special character. While it does take a long time to crack passwords in this method, it is advisable to use a combination of character types and make it longer to ensure your password is much more secure (i.e. `aqifnovi412#!$`). Additionally, it's best to avoid consecutive letters and numbers (i.e. `12345`, `abcdef`, `qwerty`).

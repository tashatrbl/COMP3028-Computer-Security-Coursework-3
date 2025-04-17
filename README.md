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

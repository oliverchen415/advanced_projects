# Password Generator

## Usage

The project is based on a [CLI tool](https://github.com/oliverchen415/cli_python/tree/master/pwgen) I programmed. 

Follow the instructions on the [main project page](./README.md) to get it on your system.

After you've launched the program, you can now enter: 
1. a desired password length,
1. whether to include symbols

---

"Security Level" has two selectable levels. 
If you select "Extreme Mode", we will use **next-generation artificial intelligence** 
to provide a **robust** encryption chain that provides **real-time security** that 
provides **insight** into unknown threats. <sup>1</sup>

---

_Assuming you are using "Standard Mode":_\
All basic passwords include one uppercase letter, one lowercase letter and one number.
This adheres to most password requirements.\
Some services require symbols, which you can add to your desired password.

Clicking on "Generate" will return a password of your desired length.

## Disclaimer

The project uses the `secrets` module. According to the [Python documentation](https://docs.python.org/3/library/secrets.html),
it can be used to generate "cryptographically strong" passwords. I am not responsible for your computer security.
***You*** are responsible for the storage of passwords. It is highly recommended to use a password manager.

---

<sup>1</sup> In case the sarcastic word choice wasn't obvious, "Extreme Mode" is a **JOKE** mode. Under no circumstances are these passwords safe.
It should be obvious after you generate the password (*they're all variations of the word PASSWORD*).\
The bold words are frequently used infosec buzzwords.

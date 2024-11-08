# Enigma Machine Explained

The Enigma Machine was an encryption device used predominantly by Nazi Germany during World War II to secure military communications. The machine utilized a complex system of rotors and wiring to create an encrypted version of a message. Each setting of the machine would produce a different encryption output, making the Enigma Machine challenging to decipher without knowing the initial settings.

## How the Enigma Machine Works

The Enigma Machine operates by substituting each letter in a message with another letter, based on a series of internal rotors and a reflector. Here’s a breakdown of its main components:

### 1. Rotors
Rotors are circular disks with electrical contacts on each side, each containing a unique wiring sequence that maps each letter to another. Each rotor can be set to a specific position (1-26), which determines the starting point for encryption.

- **Configuration**: The machine has three rotors that can be set to different initial positions. Each step advances the first rotor by one position, and after a complete rotation, it advances the second rotor.
- **Wiring**: Each rotor has a different internal wiring that creates unique letter mappings.

### 2. Reflector
The reflector is a component that bounces the signal back through the rotors. After passing through the rotors, the electrical signal reaches the reflector, which sends it back through the rotors, further scrambling the message. This dual path through the rotors makes the Enigma machine self-reciprocal, meaning the same machine settings can decrypt an encrypted message.

### 3. Stepping Mechanism
Each key press advances the first rotor by one position, changing the encryption for each subsequent character. When the first rotor completes a full rotation, it advances the second rotor, similar to an odometer. This mechanism increases the encryption’s complexity by creating a continuously changing mapping.

## Encryption Process

1. **Initial Setup**: The machine operator sets each rotor to a specific position, defining the initial encryption mapping.
2. **Character Transformation**: When a letter is entered:
   - The signal passes through the rotors, where each rotor’s wiring and current position modify the signal.
   - The signal reaches the reflector and is sent back through the rotors.
   - The output letter is displayed, representing the encrypted character.
3. **Step Advancement**: After each character, the rotors advance, changing the internal wiring mapping for the next character.

## Example

If an operator sets the rotors to positions **5-18-23** and types "HELLO":
- The machine encrypts "H" based on the rotor settings.
- The first rotor advances by one position for the next letter "E," altering the encryption mapping.
- This process repeats until the entire message is encrypted.

## Decryption

Since the Enigma Machine is reciprocal, decrypting a message is as simple as entering the encrypted message with the machine set to the original rotor positions. The message will pass back through the machine, reversing the encryption process and revealing the original text.

## Summary of Components in the Code

- **Rotors**: Defined arrays representing rotor wiring configurations.
- **Reflector**: An array that creates a reversible mapping for encryption and decryption.
- **Rotation Function**: Advances rotor positions after each character to emulate the stepping mechanism.
- **GUI (Tkinter)**: Provides a graphical interface for adjusting rotor positions, selecting encryption/decryption modes, and inputting text.

The Enigma Machine’s encryption relied on secrecy in the rotor configurations and initial settings, making it a powerful tool until its eventual cracking by Allied cryptographers. This project emulates the Enigma’s encryption mechanics, allowing users to explore this historical cipher.

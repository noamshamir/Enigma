# Enigma Machine Simulation

This project simulates the WWII-era Enigma Machine in Python, complete with a graphical interface for encryption and decryption of text. The simulation captures the core functionality of the historical Enigma, used for secure communication.

## Table of Contents
- [Overview](#overview)
- [How the Enigma Machine Works](#how-the-enigma-machine-works)
- [Features](#features)
- [Installation](#use-and-installation)
- [Code Overview](#code-overview)

## Overview

The Enigma Machine was a cipher device that encrypted messages through a series of rotating, interchangeable rotors. Each rotor mapped each letter to another in a complex, reversible way. Combined with a reflector, the machine provided highly secure, self-reciprocal encryption, where decryption could be achieved by setting the machine to the same initial configuration as used in encryption.

## How the Enigma Machine Works

1. **Rotors**: Three rotors map each letter to another based on their internal wiring. Each rotor can start at a specific position (1-26), which determines the initial encryption mapping.
2. **Reflector**: After passing through the rotors, the signal hits the reflector and returns back through the rotors, adding an additional layer of complexity.
3. **Stepping Mechanism**: Each key press rotates the first rotor by one position. After a full rotation, the next rotor advances, creating an evolving encryption pattern with each letter.

The Enigma Machine is **self-reciprocal**, meaning the same settings used to encrypt a message can be used to decrypt it.

## Features

- **Configurable Rotors**: Customize the rotor starting positions to change the encryption.
- **Encryption/Decryption Mode**: Toggle between encrypt and decrypt functions.
- **GUI Interface**: A user-friendly Tkinter-based interface for configuring the machine and viewing results.

## Use and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/enigma-simulation.git
   cd enigma-simulation
2. Ensure you have python and tkinter installed
3. Run the program:
   ```bash
   python enigma_gui.py
4. Use the interface to set rotor positions and switch between encrypt and decrypt modes.
5. Input text to see the encrypted or decrypted output.

## Code Overview
The code is divided into a few core components:

- Rotors and Reflector: Defined with specific letter mappings to simulate the historical rotor wirings.
- Initialization: The initialize_enigma() function sets the starting positions of the rotors, creating a unique encryption setup each time.
- Encryption Logic: The encrypt() function handles the character substitution based on the current rotor positions, advancing the rotors after each character for a dynamic encryption process.
- Graphical Interface: The Tkinter GUI allows users to interact with the Enigma Machine, setting rotor positions, switching modes, and inputting text.

### Example of the Encryption Flow
1. Set Initial Rotor Positions: Choose positions for rotors 1, 2, and 3.
2. Encrypt or Decrypt: Toggle between modes to either encode or decode text.
3. Process Text: Each letter input goes through the rotors, hits the reflector, and comes back, giving the encrypted/decrypted letter as output.



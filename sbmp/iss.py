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

iss_codes = {
    "ceaser_cipher.cpp": ceaser_cipher,
    "polyalphabetic_cipher.cpp": polyalphabetic_cipher,
    "row_column_transposition.cpp": row_column_transposition,
    "diffie_hellman.cpp": diffie_hellman
}

def iss_():
    for file,code in iss_codes.items():
        print(file)
    filename = input("Enter filename: ")
    with open(filename, 'w') as f:
        f.write(iss_codes[filename])
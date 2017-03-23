#include<bits/stdc++.h>
using namespace std;
 
// function to calculate Hamming distance
int hammingDist(char *str1, char *str2)
{
    int i = 0, count = 0;
    while (str1[i] != '\0')
    {
        if (str1[i] != str2[i])
            count++;
        i++;
    }
    return count;
}
 
// driver code
int main()
{
    char str1[] = "AAA+";
    char str2[] = "AAA+";
 
    // function call
    cout << hammingDist (str1, str2);
 
    return 0;
} 

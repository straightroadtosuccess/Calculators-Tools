#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    float amountu = get_float("USD amount to convert: ");
    float amountp = get_float("PHP amount to convert: ");

    float utop = 58.41;
    float ptou = 1.0 / 58.41;

    float convertedu = amountp * ptou;
    float convertedp = amountu * utop;

    printf("Converted USD amount: %2f\n", convertedu);
    printf("Converted PHP amount: %1f\n", convertedp);
}

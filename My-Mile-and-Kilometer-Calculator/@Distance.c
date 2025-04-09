#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    float mi = get_float("Miles to convert: ");
    float km = get_float("Kilometers to convert: ");

    float mitokm = 1.609344;
    float kmtomi = 0.62137;

    float convertedmi = mi * mitokm;
    float convertedkm = km * kmtomi;

    printf("Converted Miles amount: %2f\n", convertedmi);
    printf("Converted Kilometers amount: %1f\n", convertedkm);
}

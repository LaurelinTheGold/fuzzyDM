#include <stdio.h>
#include <stdlib.h>
#define BOXSIZE 256
#define PATH "/Users/richardchen/Desktop/summerResearch/2020summer/delta_T_no_halos_z012.51_nf0.981350_useTs1_zetaX2.0e+56_alphaX1.2_TvirminX2.0e+04_aveTb-56.80_Pop2_256_300Mpc"

//takes in slicefile of brightness temperature and filters to keep the ones where avgBrightTemp > 0

int main()
{
	FILE *fptr;
	float buffer;
	fptr = fopen(PATH, "rb");
	int count = 0;
	for (int i = 0; i < BOXSIZE; i++)
	{
		for (int j = 0; j < BOXSIZE; j++)
		{
			for (int k = 0; k < BOXSIZE; k++)
			{
				if (fread(&buffer, sizeof(float), 1, fptr) == 1)
				{
					if (buffer > 0)
					{
						count++;
					}
				}
				else
				{
					printf("ERROR Reading File!!\n");
				}
			}
		}
	}
	printf("Count = %d\n", count);
	double temp = count * 1.0 / 256.0 / 256 / 256;
	printf("%f\n = count / 256^3", temp);
	fclose(fptr);
	return 0;
}
// clang -Wall -g -o misc_count_GT0 misc_count_GT0.c
// Count = 113859
// 0.006787
#include <stdio.h>
#include <stdlib.h>
#define BOXSIZE 256
#define PATHC "/Users/richardchen/Desktop/summerResearch/2020summer/CDM_Tk_zprime012.51_zetaX2.0e+56_alphaX1.2_TvirminX2.0e+04_zetaIon20.00_Pop2_256_300Mpc"
#define PATHF "/Users/richardchen/Desktop/summerResearch/2020summer/FDM_Tk_zprime012.51_zetaX2.0e+56_alphaX1.2_TvirminX2.0e+04_zetaIon20.00_Pop2_256_300Mpc"
#define CMB_CONST 2.726
#define REDSHIFT 12.51

//takes in slicefile of brightness temperature and filters to keep the ones where avgBrightTemp > 0

int tcmb = CMB_CONST * (1 + REDSHIFT);

float percentVol(int count)
{
	return count * 1.0 / 256.0 / 256.0 / 256.0;
}

int main()
{
	FILE *fptrC, *fptrF;
	float bufferC;
	float bufferF;
	fptrC = fopen(PATHC, "rb");
	fptrF = fopen(PATHF, "rb");
	int countC = 0;
	int countF = 0;
	for (int i = 0; i < BOXSIZE; i++)
	{
		for (int j = 0; j < BOXSIZE; j++)
		{
			for (int k = 0; k < BOXSIZE; k++)
			{
				if (fread(&bufferC, sizeof(float), 1, fptrC) == 1) // cdm
				{
					if (bufferC >= tcmb)
					{
						countC++;
					}
				}
				else
				{
					printf("ERROR Reading File!!\n");
				}
				if (fread(&bufferF, sizeof(float), 1, fptrF) == 1) // fdm
				{
					if (bufferF >= tcmb)
					{
						countF++;
					}
				}
				else
				{
					printf("ERROR Reading File!!\n");
				}
			}
		}
	}
	printf("CountC = %d, CountF = %d\n", countC, countF);
	// double temp = count * 1.0 / 256.0 / 256 / 256;
	// printf("%f\n = count / 256^3", temp);
	printf("%%CDM = %f, %%FDM = %f\n", percentVol(countC), percentVol(countF));
	fclose(fptrC);
	fclose(fptrF);
	return 0;
}


// clang -Wall -g -o misc_count_GT_TCMB misc_count_GT_TCMB.c
// CountC = 7010642, CountF = 198873
// %CDM = 0.417867, %FDM = 0.011854

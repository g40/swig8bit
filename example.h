/* File : example.h */

#include <stdint.h>

#define dbg_printf(x,arg...) fprintf(stdout,"%s(%d): "x"\r\n",__FILE__,__LINE__,##arg)

// just stubbed
double average_i(int* buffer,int bytes)
{
	dbg_printf("average_i: %p %d",buffer,bytes);
	return 0.0;
}

// just stubbed
double average_i2(int a1,int a2,int* buffer,int bytes)
{
	dbg_printf("average_i2: %d %d %p %d",a1,a2,buffer,bytes);
	return 0.0;
}


double average_u8(unsigned char* buffer,int bytes)
{
	dbg_printf("average_u8: %p %d",buffer,bytes);
	return 0.0;
}

double average_s8(char* buffer,int bytes)
{
	dbg_printf("average_s8: %p %d",buffer,bytes);
	return 0.0;
}


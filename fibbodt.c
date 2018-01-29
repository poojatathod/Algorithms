#include<stdio.h>

long int fibbo(long int n,long int arr[])
{
  if(arr[n-1]!=-1)
  {
    return arr[n];
  }
  else
  {
  arr[n]=(fibbo((n-1),arr) +fibbo((n-2),arr));
  return arr[n];
  }
}


int main()
{
  int n=0,i;
  long int output=0;

  printf("Enter a value of n:");
  scanf("%d",&n);
  long int arr[n];
  for(i=0;i<n;i++)
  {
    arr[i]=-1;
  }
  arr[0]=0;
  arr[1]=1;

  output=fibbo(n-1,arr);
  printf("fibbonaci element at %d  position is: %ld\n",n,output);
}


""" 
A) Yukarı verilen dizinin sort türüne göre aşamalarını yazınız.
1-) [22,27,16,2,18,6]
2-) 22|,27,16,2,18,6
3-) 22,27|,16,2,18,6
4-) 22,16,27|,2,18,6
5-) 16,22,27|,2,18,6
6-) 16,22,2,27|,18,6
7-) 16,2,22,27|,18,6
8-) 2,16,22,27|,18,6
9-) 2,16,22,18,27|,6
10-) 2,16,18,22,27|,6
11-) 2,16,18,22,6,27|
12-) 2,16,18,6,22,27|
13-) 2,16,6,18,22,27|
14-) 2,6,16,18,22,27|

B) Big-O gösterimini yazınız.
O(N^2)

C) Time Complexity: Average case: Aradığımız sayının ortada olması,Worst case: Aradığımız sayının sonda olması, Best case: Aradığımız sayının dizinin en başında olması.
Dizi sıralandıktan sonra 18 sayısı hangi case kapsamına girer? Yazınız.

Worst Case:
Küçükten büyüğe sıralanmak istenen bir dizinin tüm elemanlarının büyükten küçüğe sıralanmasıdır (reversed order).
O(N x (N+1)) / 2 => O((N²+N)/2) => O(N²/2) => O(N²)

Best Case:
Küçükten büyüğe sıralamak istediğimiz bir dizinin elemanlarının zaten küçükten büyüğe sıralandığı durumdur.
Dolayısıyla O(N)' dir.

Average Case:
O(N²) + O(N) in ortalaması olacağı için yine N² cinsinden bir sonuç olur. Average case = O(N²)

[2,6,16,18,22,27]=> Sıralanmış dizi

Cevap : Aradığımız sayı başta(Best Case) ve sonda(Worse Case) olmadığından beklenilen durum olarak Average Case'dir.

SORU-2) [7,3,5,8,2,9,4,15,6] dizisinin Insertion Sort'a göre ilk 4 adımını yazınız.
7|,3,5,8,2,9,4,15,6
3,7|,5,8,2,9,4,14,6
3,5,7|,8,2,9,4,14,6
3,5,7,8|,2,9,4,14,6 ->4.adımımız bu şekilde olur"""

#include <stdio.h>
#define MAX 50
void insertionsort(int arr[],int size)
{
 int i,j,element;
 for(i=0;i<size;i++)
 {
  element = arr[i];
  j=i-1;
  
  
  while(j>=0 && arr[j] > element)
  {
   arr[j+1] = arr[j];
   j--;
  }
  arr[j+1] = element;
    }
}
int main(){
 int array[MAX];
 int i,size;
 
 printf("size> ");
 scanf("%d",&size);
 
 printf("%d tane eleman giriniz> ",size);
 for(i=0;i<size;i++)
 {
  scanf("%d",&array[i]);
 }
 
 insertionsort(array,size);
 for(i=0;i<size;i++)
 {
  printf("%d ",array[i]);
 }
 
 
 return 0;
}


#https://app.patika.dev/ressuv
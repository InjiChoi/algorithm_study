#include <stdio.h>

int arr[10000001]={0,1};

int main(){
    int n,m;
    int nnum, mnum;

    scanf_s("%d",&n);

    for (int i=0;i<n;i++){
        scanf_s("%d", &nnum);
        arr[nnum]=1;
    }

    scanf_s("%d",&m);

    for (int i=0;i<m;i++) {
        scanf_s("%d", &mnum);
        printf("%d ", arr[mnum]);
    }
    return 0;
}
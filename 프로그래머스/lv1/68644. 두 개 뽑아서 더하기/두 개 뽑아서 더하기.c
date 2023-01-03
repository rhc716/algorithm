#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#define SWAP(a,b) {int c; c=a; a=b; b=c;}

// numbers_len은 배열 numbers의 길이입니다.
int* solution(int numbers[], size_t numbers_len) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int k = 0;
    int temp;
    int flag;
    
    int* answer = (int*)malloc(sizeof(int) * numbers_len * 10);
    for (int i = 0; i < numbers_len; i++)
    {
        for (int j = i + 1; j < numbers_len; j++)
        {
            temp = numbers[i] + numbers[j];
            flag = 0;
            for (int c = 0; c < k; c++)
            {
                if (answer[c] == temp)
                {
                    flag = 1;
                }
            }
            if (flag == 0)
            {
                answer[k++] = numbers[i] + numbers[j];
            }
        }
    }
    for (int i = 0; i < k; i++)
    {
        for (int j = 0; j < k - 1; j++){
            if (answer[j] > answer[j + 1])
                SWAP(answer[j], answer[j + 1]);
        }
    }
    return answer;
}
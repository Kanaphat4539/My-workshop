#include <stdio.h>

char calculateGrade(float score) {
    if (score >= 80) return 'A';
    else if (score >= 70) return 'B';
    else if (score >= 60) return 'C';
    else if (score >= 50) return 'D';
    else return 'F';
}

int main() {
    float score;
    
    printf("Enter your score: ");
    scanf("%f", &score);
    
    if (score < 0 || score > 100) {
        printf("Invalid score. Please enter a number between 0 and 100.\n");
    } else {
        char grade = calculateGrade(score);
        printf("Your grade is: %c\n", grade);
    }
    
    return 0;
}

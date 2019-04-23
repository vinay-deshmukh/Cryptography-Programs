#include<stdio.h>
#include<string.h>

int main(){
    char actual_pwd[5] = "0123";
    char u_pwd[5]; // user password
    char* flag = u_pwd;

    flag = u_pwd + sizeof(u_pwd);


    // Initialize as not logged in
    *flag = 'f';


    printf("Enter password:");
    gets(u_pwd); // reads input till newline

    printf("Entered: =%s=\n", u_pwd);
    printf("Actual : =%s=\n", actual_pwd);

    // check password
    if(strcmp(u_pwd, actual_pwd) != 0){
        // not same
        printf("password is wrong! try again\n");
    }
    else{
        // same
        printf("Password is correct!\n");
        *flag = 't';
        
    }

    if(*flag == 't'){
        printf("You have been logged in!\n");
    }
    else{
        printf("You are not logged in!\n");
    }

    return 0;
}
/*
Compile with -fstack-protector (atleast on Windows)
On some linux distros, this is on by default for gcc
ie
gcc file.c -fstack-protector
to preserve declaration order of the arrays ie stack variables


Case 1) Entering correct password, and user gets verified!
Enter password:0123
Entered: =0123=
Actual : =0123=
Password is correct!
Welcome!

Case 2) Entering wrong password, and not being verified!
Enter password:flsdj
Entered: =flsdj=
Actual : =0123=
password is wrong! try again
You are not logged in!

Case 3) Causing buffer overflow, such that `flag` will contain the value 't'
this is possible since `flag` is pointing to the location after `u_pwd`,
which takes input from user.
Enter password:01234t
Entered: =01234t=
Actual : =0123=
password is wrong! try again
You have been logged in!


*/
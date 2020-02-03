
/*---------------------------------------------------------*/ 
/*   Modified md5 hash                          J.Bardus   */
/*   Check if username and password are valid.             */
/*                                                         */
/*   I set up this exra secure password checker to         */
/*   validate username/password in the 'latest development */
/*   and patents' - section.                               */
/*                                                         */
/*   Since some users -and even administrators-            */
/*   use short passwords I make this a bit more            */
/*   secure. A less than 4 chars password is filled        */
/*   up with some extra characters.                        */
/*   The hash is built from a string which is built        */
/*   by concatenating username and password.               */
/*   I use my own modified md5-algo with an additional     */
/*   XOR, which is performed at different stages in        */
/*   the md5-algo.                                         */
/*   This all together makes it impossible to reverse      */
/*   or brute force this algo.                             */
/*   (The good old security through obscurity though)      */
/*---------------------------------------------------------*/


/*-------------  includes ---------------------------------*/
#include <stdio.h>
#include "mymd5.h"
/*---------------------------------------------------------*/


/*-----------  prototypes ---------------------------------*/
char checkit(char* username, char* password, char* hash);
/*---------------------------------------------------------*/


/*-----------  defines ------------------------------------*/
#define MY_MD5_XOR = 31337
/*---------------------------------------------------------*/


/*------------- main --------------------------------------*/
int main(int argc, char* argv[])
{

 /* test if all arguments are given */
 if (argc<4)  { 
   printf("\nusage: chkuserpass username password <hash>\n"); 
   return 1; 
 }


 /*   call the check routine and print result to stdout  */ 
 if (checkit(argv[1], argv[2], argv[3]) == 'Y')  
   printf("correct"); 
 else
   printf("notvalid");


return 0;
}
/*---------------------------------------------------------*/




/*---------------------------------------------------------*/
/*  checks given username and password                     */
/*  return value: 'Y' or 'N'                               */
/*---------------------------------------------------------*/
char checkit(char* username, char* password, char* hash)
{
 char is_pass_correct = 'N';   /* initialize to NO          */
 char *fillstring = "_T*4$n";  /* Use this string to make a */
                               /* less than 4chars password */
                               /* longer                    */
 char concatenated[200];
 strcpy(concatenated, username);

 /*  if a password is less than 4 chars long,  */
 /*  add some extra characters                 */
 if (strlen(password) < 4)
   strcat(concatenated, fillstring);

 strcat(concatenated, password);

 if (strcmp(mymd5(concatenated), hash) == 0) 
   is_pass_correct = 'Y';

return is_pass_correct;
}
/*---------------------------------------------------------*/

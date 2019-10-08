import os
import subprocess

line_found=False
dig_domain=os.system("dig detik.com > temp")
get_answer_line=int(subprocess.check_output("cat temp| grep -n 'ANSWER SECTION' | cut -d: -f1", shell=True).decode("utf-8"))

if get_answer_line!=0:
    temp=open("temp", "r")
    per_line=temp.read().splitlines()
    text_len=len(per_line)
    the_answer=''

    while get_answer_line < text_len:
        if per_line[get_answer_line].startswith(";;"):
            break;
        else:
            the_answer+='\n'+per_line[get_answer_line]

        get_answer_line+=1

    print(the_answer.strip())

os.system("rm temp")
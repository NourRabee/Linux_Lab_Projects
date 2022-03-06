#Nour_Rabee_1191035
#asking the user to enter the name of the content file
echo "Please enter the name of the content file."
read filename

if [ ! -e $filename ] # if the file does not exist
then
#raising an error message if the file does not exist
  echo "file does not exist! Please try again!"
  exit 1
else
   while(true)
   do
   #showing the available operations
   printf "\n****Welcome to Contact Managment System****\n
         \tMAIN MENU\t
       ================================
          [1] Add a new Contact
          [2] List all Contacts
          [3] Search for Contact
          [4] Edit a contact
          [5] Delete a Contact
          [6] Exit
      ==================================
        Enter a choice:"
   read choice

   #The case command
   case "$choice"
        in

        1)
                 #############Add a new contact##############

contactInfo=""
printf " Please enter the First name: (not optional)\n"
read Fname
contactInfo+="$Fname"

while(true)
do
printf "Do you want to insert the last name?(optional), answer by yes or no\n"
read answer
if [ $answer = "yes" ]
then
  echo "Please enter the last name:"
  read Lname
  contactInfo+=", $Lname"
break
elif [ $answer = "no" ]
then
break
else
 echo "Oops!Invalid input, please try again"
continue
fi
done
######################
while(true)
do
   numberOfDigits=0

   echo "please enter the phone number,from 9 to 10 numbers(not optional)"
   read phoneNum
   if [[ $phoneNum =~ [^[:digit:]] ]] #???????
   then
     echo "Try again! This phone number consists of nondigit elements!!"
     continue
   else
         digitsNum=$( echo -n "$phoneNum" | wc -c) #-n -- > string is not null
         if [ "$digitsNum" -eq 9 -o "$digitsNum" -eq 10 ]
         then
           contactInfo+=", $phoneNum"
           break
         else
         echo "Invalid phone Number, the length of it must be up to 9 or 10 digits"
         continue
         fi
   fi
done
#######################

while(true)
do
printf "Do you want to insert the email address? answer by yes or no\n"
read answer2
if [ $answer2 = "yes" ]
then
   echo "please enter the email address:"
   read email
  if [[ $email == "@" ]] # ** means a substring of a string
  then
    contactInfo+=", $email"
     break
   else
   echo "Invalid Email, please try again and make sure you press'@'"
    continue
    fi
elif [ $answer2 = "no" ]
then
break
else
echo "Oops!Invalid input, try again"
continue
fi
done
#########
echo "$contactInfo" >> contact.txt
printf "\n"
cat $filename
;;

        2) printf "\n"

while(true)
do
printf "Do you want to list the contacts based on:
        [1] First name
        [2] Last name
        [3] Exit
      ============================
       Enter your choice:"
read choice

if [ $choice -eq 1 ]
then
sort -k1 $filename > sorting.txt 
#sorting data based on the first column "first name"

  printf " Which Fields do you want to show?
           [1] First name
           [2] Last name
           [3] Phone Number
           [4] Email
           [5] Exit
     ===============================
           Enter your choice:"
read choice
if [ $choice -eq 1 ]
then

cut -d "," -f1 sorting.txt #-d stands for delimiter

elif [ $choice -eq 2 ]
then

while read line
do
N=$(echo $line | tr -dc "," | wc -c) # delete everything except commas 
N=$(($N+1))

if [ $N -eq 4 ]
then
echo $line | cut -d "," -f2

elif [ $N -eq  3 ]
then
if [[ $line != "@" ]]
then
echo $line | cut -d "," -f2
fi
fi
done < sorting.txt

elif [ $choice -eq 3 ]
then
grep '[0-9][0-9]*' sorting.txt > info.txt #searching for all the lines that matches any digits followed by zero or more digits.

while read line
do
N=$(echo $line | tr -dc "," | wc -c)
N=$(($N+1))

if [ $N -eq 4 ]
then
echo $line | cut -d "," -f3
elif [ $N -eq 2 ]
then
echo $line | cut -d "," -f2
elif [ $N -eq  3 ]
then
if [[ $line == "@" ]]
then
echo $line | cut -d "," -f2
else
echo $line | cut -d "," -f3
fi
fi
done < info.txt


elif [ $choice -eq 4 ]
then
grep "@" sorting.txt > info.txt #searching for all lines that contains @ and transfer them to info,txt

while read line
do
N=$(echo $line | tr -dc "," | wc -c)
N=$(($N+1))

if [ $N -eq 4 ]
then
echo $line | cut -d "," -f4
elif [ $N -eq  3 ]
then
if [[ $line == "@" ]]
then
echo $line | cut -d "," -f3
fi
fi
done < info.txt

elif [ $choice -eq 5 ]
then
continue

else
echo "Invalid input , please try again"
fi

elif [ $choice -eq 2 ]
then
while read line
do
N=$(echo $line | tr -dc "," | wc -c)
N=$(($N+1))

if [ $N -eq 4 ]
then
echo $line >> lastname.txt

elif [ $N -eq  3 ]
then
if [[ $line != "@" ]]
then
echo $line >> lastname.txt
fi
fi
done < $filename

sort -k2 lastname.txt > sorting.txt
cat /dev/null > lastname.txt
#clearing the file

printf " Which Fields do you want to show?
           [1] First name
           [2] Last name
           [3] Phone Number
           [4] Email
           [5] Exit
     ===============================
           Enter your choice:"

read choice

if [ $choice -eq 1 ]
then
cut -d "," -f1 sorting.txt

elif [ $choice -eq 2 ]
then
cut -d "," -f2 sorting.txt

elif [ $choice -eq 3 ]
then
cut -d "," -f3 sorting.txt

elif [ $choice -eq 4 ]
then
cut -d "," -f4 sorting.txt

elif [ $choice -eq 5 ]
then
continue
else
echo "inavlid input! please try again"
fi

elif [ $choice -eq 3 ]
then
break
else
echo "Invalid input, please try again!"
fi
done

;;

#List all contacts

        3)

echo " please enter any info about that contact you are searching for:"
read info

N=$(echo $info | tr -dc " " | wc -c)
N=$(($N+1))

if [ $N -eq 1 ]
then
grep -i "$info" contact.txt #-i ignore uppercase vs. lowercase for matching and display them 

elif [ $N -eq 2 ]
then
first=$(echo $info | cut -d " " -f1 )
second=$(echo $info | cut -d " " -f2 )

while read line
do

echo $line | tr "," " " | grep -i ".*$first.*$second.*"

done < contact.txt

elif [ $N -eq 3 ]
then
first=$(echo $info | cut -d " " -f1 )
second=$(echo $info | cut -d " " -f2 )
third=$(echo $info | cut -d " " -f3 )
while read line
do

echo $line | tr "," " " | grep -i ".*$first.*$second.*$third.*"

done < contact.txt

elif [ $N -eq 4 ]
then
first=$(echo $info | cut -d " " -f1 )
second=$(echo $info | cut -d " " -f2 )
third=$(echo $info | cut -d " " -f3 )
fourth=$(echo $info | cut -d " " -f4 )

while read line
do

echo $line | tr "," " " | grep -i ".*$first.*$second.*$third.*$fourth.*"

done < contact.txt

fi
;;

        4)
cat -n $filename 
echo "PLease enter the number of line you want to edit:\n"
read n
line=$(head -n $n $filename | tail -1 )
echo $line
N=$(echo $line | tr -dc "," | wc -c)
N=$(($N+1))

while true; do
if [ $N -eq 4 ]
then
printf " which field do you want to edit?
    ======================================
        [1] First name
        [2] Last name
        [3] phone number
        [4] Email address
        [5] Exit
       =============================
        Enter your choice:"
read choice
if [ $choice -eq 1 ]
then
  name=$(echo $line | cut -d "," -f1 )
  echo "Please enter the new first name:"
  read newname
  
  #s in sed to search and replace
  sed -i ""$n"s/$name/$newname/g" $filename
  
elif [ $choice -eq 2 ]
then
 echo "Please enter the new last name:"
 read last
 Lname=$(echo $line | cut -d "," -f2 )
 sed -i ""$n"s/$Lname/$last/g" $filename
elif [ $choice -eq 3 ]
then
 echo "Please enter the new phone number:"
 read phone
 if [[ "$phone" =~ [^[:digit:]] ]]
   then
     echo "Try again, the phone number must consist only of digit numbers"
 else
     digitsNum=$(echo -n "$phone" | wc -c)
     if [ "$digitsNum" -eq 9 -o "$digitsNum" -eq 10 ]
     then
       phoneNum=$(echo $line | cut -d "," -f3 )
       sed -i ""$n"s/$phoneNum/$phone/g" $filename
     else
       echo "Invalid phone number, the length if it must be 9 to 10 digits"
     fi
 fi
elif [ $choice -eq 4 ]
then
echo "please enter the new email:"
read email
if [[ $email == "@" ]]
then
   emailAddress=$(echo $line | cut -d "," -f4 )
   sed -i ""$n"s/$emailAddress/$email/g" $filename
else
   echo "Invalid Email, make sure you press '@'"
fi
elif [ $choice -eq 5 ]
then
break
else
echo "invalid option! please try again"
fi

elif [ $N -eq 2 ]
then

printf "which fields do you want to edit?
    ======================================
        [1] Fisrt name
        [2] Phone number
        [3] Exit
       =============================
        Enter your choice:"
read choice
if [ $choice -eq 1 ]
then
name=$(echo $line | cut -d "," -f1 )
echo "Please enter the new fisrt name:"
read new
sed -i ""$n"s/$name/$new/g" $filename
elif [ $choice -eq 2 ]
then
echo "Please enter the new phone number:"
read phone
if [[ "$phone" =~ [^[:digit:]] ]]
then
 echo "Try again, the phone number must consist only of digit numbers"
else
  digitsNum=$(echo -n "$phone" | wc -c)
  if [ "$digitsNum" -eq 9 -o "$digitsNum" -eq 10 ]
  then
     phoneNum=$(echo $line | cut -d "," -f2 )
     sed -i ""$n"s/$phoneNum/$phone/g" $filename
  else
    echo "Invalid phone number, the length if it must be 9 to 10 digits"
  fi
fi
elif [ $choice -eq 3 ]
then
exit 0
else
echo "Invalid input! Please try again !"
fi

elif [ $N -eq 3 ]
then
if [[ $line != "@" ]]
then
printf "which fields do you want to edit?
    ======================================
        [1] Fisrt name
        [2] Last name
        [3] Phone number
        [4] Exit
       =============================
        Enter your choice:"
read choice
if [ $choice -eq 1 ]
then
name=$(echo $line | cut -d "," -f1 )
echo "Please enter the new Fisrt name:"
read new
sed -i ""$n"s/$name/$new/g" $filename
elif [ $choice -eq 2 ]
then
echo "Please enter the new Last name:"
read last
Lname=$(echo $line | cut -d "," -f2 )
sed -i ""$n"s/$Lname/$last/g" edit.txt
elif [ $choice -eq 3 ]
then
echo "Please enter the new phone number:"
read phone
if [[ "$phone" =~ [^[:digit:]] ]]
then
 echo "Try again, the phone number must consist only of digit numbers"
else
  digitsNum=$(echo -n "$phone" | wc -c)
  if [ "$digitsNum" -eq 9 -o "$digitsNum" -eq 10 ]
  then
   phoneNum=$(echo $line | cut -d "," -f3 )
   sed -i ""$n"s/$phoneNum/$phone/g" $filename
  else
   echo "Invalid phone number, the length if it must be 9 to 10 digits"
  fi
fi
elif [ $choice -eq 4 ]
then
exit 0
else
echo "Invalid input! please try again."
fi

else
printf "which fields do you want to edit?
    ======================================
        [1] Fisrt Name
        [2] Phone Number
        [3] Email Address
        [4] Exit
       =============================
        Enter your choice:"
read choice
if [ $choice -eq 1 ]
then
name=$(echo $line | cut -d "," -f1 )
echo "Please enter the new Fisrt name:"
read new
sed -i ""$n"s/$name/$new/g" $filename
elif [ $choice -eq 2 ]
then
echo "Please enter the new phone number:"
read phone
if [[ "$phone" =~ [^[:digit:]] ]]
then
 echo "Try again, the phone number must consist only of digit numbers"
else
  digitsNum=$(echo -n "$phone" | wc -c)
  if [ "$digitsNum" -eq 9 -o "$digitsNum" -eq 10 ]
  then
    phoneNum=$(echo $line | cut -d "," -f2 )
    sed -i ""$n"s/$phoneNum/$phone/g" $filename
  else
   echo "Invalid phone number, the length if it must be 9 to 10 digits"
  fi
fi

elif [ $choice -eq 3 ]
then
echo "please enter the new email:"
read email
if [[ $email == "@" ]]
 then
   emailAddress=$(echo $line | cut -d "," -f4 )
   sed -i ""$n"s/$emailAddress/$email/g" $filename
 else
     echo "Invalid Email, make sure you press '@'"
fi
elif [ $choice -eq 4 ]
then
exit 0
else
echo "Invalid input! please try again."
fi
fi
fi
done
cat $filename
;;
        5)
           cat -n $filename
          echo "Please enter the number of the contact you want to delete"
          read n

          #To directly modify on file we use -i with sed
           sed -i "$n"d $filename
           cat -n $filename ;;
#Delete a contact
        6) echo " Exit from the Program"
           exit 0
           ;;
#Exit
        *)echo "Bad argument!! please choose a choice from the main menu."
   esac


done
fi

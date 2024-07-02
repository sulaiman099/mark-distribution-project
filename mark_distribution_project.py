class Computer:
    def first_project(self,num1,num2,num3):
        
        F_project=num1+num2+num3
        return F_project

    def second_project(self,num1,num2,num3):
        S_project=num1+num2+num3
        return S_project

    def Third_project(self,num1,num2,num3):
        T_project=num1+num2+num3
        return T_project
    
    def sub_winner(self,f_result,s_result,t_result):
        if f_result>s_result and f_result>t_result:
            print(f'\ncongratulation Computer Technology of Frist Project')
            return f_result
        elif s_result>f_result and s_result>t_result:
            print(f'\ncongratulation Computer Technology of Second Project')
            return s_result
        else:
            print(f'\ncongratulation Computer Technology of Third Project')
            return t_result
        
    

class Civil:
    def first_project(self,num1,num2,num3):
        A_project=num1+num2+num3
        return A_project

    def second_project(self,num1,num2,num3):
        B_project=num1+num2+num3
        return B_project

    def Third_project(self,num1,num2,num3):
        C_project=num1+num2+num3
        return C_project
    
    def sub_winner(self,f_result,s_result,t_result):
        if f_result>s_result and f_result>t_result:
            print(f'\ncongratulation Civil Technology of Frist Project')
            return f_result
        elif s_result>f_result and s_result>t_result:
            print(f'\ncongratulation Civil Technology of Second Project')
            return s_result
        else:
            print(f'\ncongratulation Civil Technology of Third Project')
            return t_result


class Electrical:
    def first_project(self,num1,num2,num3):
        D_project=num1+num2+num3
        return D_project

    def second_project(self,num1,num2,num3):
        E_project=num1+num2+num3
        return E_project

    def Third_project(self,num1,num2,num3):
        F_project=num1+num2+num3
        return F_project
    
    def sub_winner(self,f_result,s_result,t_result):
        if f_result>s_result and f_result>t_result:
            print(f'\ncongratulation Electrical Technology of Frist Project')
            return f_result
        elif s_result>f_result and s_result>t_result:
            print(f'\ncongratulation Electrical Technology of Second Project')
            return s_result
        else:
            print(f'\ncongratulation Electrical Technology of Third Project')
            return t_result

class Result:
    def result(self,win_c,win_cv,win_e):
        if win_c>win_cv and win_c>win_e:
            print('\nFinally congratulation computer technology')
        elif win_cv>win_c and win_cv>win_e:
            print('\nFinally congratulation civil technology')
        else:
            print('\nFinally congratulaion Electrical technology')
    
    

print('List Of Registered Technologies')
print('computer','civil','electrical')#ai list a jara age thakbe tader input age dite hobe

while True:
   
    Technology=input('Enter the technology name:')
    if Technology=='computer':
        print('\nfirst project:')
        num1=int(input('\tEnter the first mark:'))
        num2=int(input('\tEnter the second mark:'))
        num3=int(input('\tEnter the third mark:'))
        c_ans=Computer()
        f_result=c_ans.first_project(num1,num2,num3)
        print(f'F_project of total mark:{f_result}')#F_projec demo name

        print('\nsecond project:')
        num1=int(input('\tEnter the first mark:'))
        num2=int(input('\tEnter the second mark:'))
        num3=int(input('\tEnter the third mark:'))
        c_ans=Computer()
        s_result=c_ans.second_project(num1,num2,num3)
        print(f'S_project of total mark:{s_result}')#S_projec demo name

        print('\nthird project:')
        num1=int(input('\tEnter the first mark:'))
        num2=int(input('\tEnter the second mark:'))
        num3=int(input('\tEnter the third mark:'))
        c_ans=Computer()
        t_result=c_ans.Third_project(num1,num2,num3)
        print(f'T_project of total mark:{t_result}')#T_projec demo name

        win_c=c_ans.sub_winner(f_result,s_result,t_result)
    


   
    if Technology=='civil':
        print('\nfirst project')
        num1=int(input('\tEnter the first mark:'))
        num2=int(input('\tEnter the second mark:'))
        num3=int(input('\tEnter the third mark:'))
        cv_ans=Civil()
        f_result=cv_ans.first_project(num1,num2,num3)
        print(f'A_project of total mark:{f_result}')#A_projec demo name

        print('\nsecond project')
        num1=int(input('\tEnter the first mark:'))
        num2=int(input('\tEnter the second mark:'))
        num3=int(input('\tEnter the third mark:'))
        cv_ans=Civil()
        s_result=cv_ans.second_project(num1,num2,num3)
        print(f'B_project of total mark:{s_result}')#B_projec demo name

        print('\nthird project')
        num1=int(input('\tEnter the first mark:'))
        num2=int(input('\tEnter the second mark:'))
        num3=int(input('\tEnter the third mark:'))
        cv_ans=Civil()
        t_result=cv_ans.Third_project(num1,num2,num3)
        print(f'C_project of tatal mark:{t_result}')#C_projec demo name

        win_cv=cv_ans.sub_winner(f_result,s_result,t_result)




    if Technology=='electrical':
        print('\nfirst project')
        num1=int(input('\tEnter the first mark:'))
        num2=int(input('\tEnter the second mark:'))
        num3=int(input('\tEnter the third mark:'))
        e_ans=Electrical()
        f_result=e_ans.first_project(num1,num2,num3)
        print(f'D_project of total mark:{f_result}')#D_projec demo name

        print('\nsecond project')
        num1=int(input('\tEnter the first mark:'))
        num2=int(input('\tEnter the second mark:'))
        num3=int(input('\tEnter the third mark:'))
        e_ans=Electrical()
        s_result=e_ans.second_project(num1,num2,num3)
        print(f'E_project of total mark:{s_result}')#E_projec demo name

        print('\nthird project')
        num1=int(input('\tEnter the first mark:'))
        num2=int(input('\tEnter the second mark:'))
        num3=int(input('\tEnter the third mark:'))
        e_ans=Electrical()
        t_result=e_ans.Third_project(num1,num2,num3)
        print(f'F_project of total mark:{t_result}')#F_projec demo name

        win_e=e_ans.sub_winner(f_result,s_result,t_result)




        finall=Result()
        finall.result(win_c,win_cv,win_e)
        break
    
        
    
    


        
    


        
    
        

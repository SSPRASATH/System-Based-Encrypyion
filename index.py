""" Shamir Secrete Sharing implementation """
""" Developed by SP """

#import
import os
import random


#banner creation
banner =                                                                                            """                  
   SSSSSSSSSSSSSSS hhhhhhh                                                         iiii                     
 SS:::::::::::::::Sh:::::h                                                        i::::i                    
S:::::SSSSSS::::::Sh:::::h                                                         iiii                     
S:::::S     SSSSSSSh:::::h                                                                                  
S:::::S             h::::h hhhhh         aaaaaaaaaaaaa      mmmmmmm    mmmmmmm   iiiiiiirrrrr   rrrrrrrrr   
S:::::S             h::::hh:::::hhh      a::::::::::::a   mm:::::::m  m:::::::mm i:::::ir::::rrr:::::::::r  
 S::::SSSS          h::::::::::::::hh    aaaaaaaaa:::::a m::::::::::mm::::::::::m i::::ir:::::::::::::::::r 
  SS::::::SSSSS     h:::::::hhh::::::h            a::::a m::::::::::::::::::::::m i::::irr::::::rrrrr::::::r
    SSS::::::::SS   h::::::h   h::::::h    aaaaaaa:::::a m:::::mmm::::::mmm:::::m i::::i r:::::r     r:::::r
       SSSSSS::::S  h:::::h     h:::::h  aa::::::::::::a m::::m   m::::m   m::::m i::::i r:::::r     rrrrrrr
            S:::::S h:::::h     h:::::h a::::aaaa::::::a m::::m   m::::m   m::::m i::::i r:::::r            
            S:::::S h:::::h     h:::::ha::::a    a:::::a m::::m   m::::m   m::::m i::::i r:::::r            
SSSSSSS     S:::::S h:::::h     h:::::ha::::a    a:::::a m::::m   m::::m   m::::mi::::::ir:::::r            
S::::::SSSSSS:::::S h:::::h     h:::::ha:::::aaaa::::::a m::::m   m::::m   m::::mi::::::ir:::::r            
S:::::::::::::::SS  h:::::h     h:::::h a::::::::::aa:::am::::m   m::::m   m::::mi::::::ir:::::r            
 SSSSSSSSSSSSSSS    hhhhhhh     hhhhhhh  aaaaaaaaaa  aaaammmmmm   mmmmmm   mmmmmmiiiiiiiirrrrrrr      Secret Sharing"""

about = """Shamir's Secret Sharing is an algorithm in cryptography created by Adi Shamir. 
It is a form of secret sharing, where a secret is divided into parts, giving each participant its own unique part,
where some of the parts or all of them are needed in order to reconstruct the secret.
Counting on all participants to combine the secret might be impractical, and therefore sometimes the threshold scheme is used 
where any {\displaystyle k} k of the parts are sufficient to reconstruct the original secret. """

""" def main():
    print ""
    print "----------------------------------------------------------------------------------------------------------------------   "
    print "OPTIONS"
    print "\n 1. CREATE SECRETE"
    print "\n 2. DECRYPT SECRETE"
    print "\n 3. ABOUT"
    option = raw_input("\n Enter the option > ")
    if option == "3":
        os.system('clear')
        print banner
        print "\n\n\n",about
        ino = raw_input("\n\nPress Enter to exit")
        if ino :
            exit()
 """


 
def autogenpoly():
    Secret = 1234
    N = raw_input("Enter the Total number of shares >")
    for x in range(int(N)):
        a = random.randint(1,9999)
        print a
        print x
        print a+Secret


if __name__ == "__main__":
    os.system('clear')
    autogenpoly()
 #   print banner
#    main()
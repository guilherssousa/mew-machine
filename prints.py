def start():
    print("""
,--.   ,--.,------.,--.   ,--.    ,--.   ,--.  ,---.   ,-----.,--.  ,--.,--.,--.  ,--.,------. 
|   `.'   ||  .---'|  |   |  |    |   `.'   | /  O  \ '  .--./|  '--'  ||  ||  ,'.|  ||  .---' 
|  |'.'|  ||  `--, |  |.'.|  |    |  |'.'|  ||  .-.  ||  |    |  .--.  ||  ||  |' '  ||  `--,  
|  |   |  ||  `---.|   ,'.   |    |  |   |  ||  | |  |'  '--'\|  |  |  ||  ||  | `   ||  `---. 
`--'   `--'`------''--'   '--'    `--'   `--'`--' `--' `-----'`--'  `--'`--'`--'  `--'`------' 

Mew Machine Script v1.0
A tool to generate a nearly-legit YOSHIRA Mew in your Pokemon Red/Blue/Yellow save file.
We recommend you to backup your game progress before trying this tool.
This is not a official or licensed Nintendo product.
Built by guilherssousa https://github.com/guilherssousa"
    """)

def ascii_mew():
    print("""
                     .^!J^                                  
                  .~JG##G:                                  
                ^JGB#BBJ.                                   
             .!YPPPP5?^.^~~!7YPG5.                          
           :75P55PP5?JPB#######BG!                          
         .75PP5JB####&&###BBBBBBB5:                         
        !YJ7~^. 7B#######BBBGP55B#G:                        
      ^?7:      :BBGPGBBBBBGBP?!P#B:                        
     !?:        !#G#57GBBBBBG#5PG5^ .::^^^^^^^~^~~~~~~~^    
    !7          .JGBBYP#BBBBBG55?~~~~^:...            .!!   
   ~7             .~7J5GBBBGPYY55PPGGPPP!             :J^   
   !!.         ..:^^^^^!YPP555PGBBP!^~!7:           :77:    
    :~^^^^^^^^^^::.  ~PG5?!^Y###BBBP!.           .~77:      
                     :~.    J###BBBB#GY~.     .:!7~.        
                            5####BBBBB#BG7.:^~~^.           
                           ~G#####BG#BBBB#5!:.              
                           5B#####BGGBB###B:                
                           JBGB##BBG55PPPP57.               
                           ?55Y?JJYYJ7^..~5PJ               
                           ~555:          ?PG?              
                           .PGGP:         ^BB#J             
                            !BBBP^         P###?            
                             !GBB7         ?####7           
                              .~~.         ~#####:          
                                           .PB&BB~          
                                            .~??^           
    """)

def certificate_of_authenticity(tid):
    print("""
___________________________________________________________ 
|  _______________________________________________________  |
| | 
                Certificate of Authenticity

                    Trainer ID: {}
| |
| |_______________________________________________________| |
|___________________________________________________________|
        """.format(str(tid).rjust(5, '0')))
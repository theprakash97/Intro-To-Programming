
Both output & input mechanisms are used in programming to interact with the outer-world. The output mechanism 
used to produce final-output of program for standard output-devices(terminal, files, printer, speaker, etc).
The input mechanism used to get inputs from the standard input-devices (keyboard, scanner, mouse, touchpad, voice-command, read from files on server , etc) .

Output can take various forms depending on the nature of the program and its intended purpose : 

`Console Output`     : This is text or data that is displayed in the console or 
                         command-line interface . 

`Graphical Output`   : In applications with a graphical user interface ( GUI ) , output can be visual elements 
                         such as :  windows, buttons, images, charts, graphs, or animations. 

`Files`              : Programs often produce output that is stored in files on disk. This can include text files, 
                         binary files, databases, spreadsheets, images, audio files, and more. File output allows programs to save data for later use, share it with other programs, or provide it to users in a persistent format.

`Network Output`     : Some programs generate output that is transmitted over a network to other devices or systems. 
                         This can include sending data to servers, communicating with other programs through APIs (Application Programming Interfaces), or streaming media content over the internet.

`Hardware output`    : In embedded systems or low-level programming, output can involve controlling hardware 
                         components  such as LEDs, motors, sensors, displays, or actuators. Programs send signals or commands to these devices to produce physical effects in the real world.

`Error output`       : When a program encounters an error or exception, it may produce error messages or 
                         diagnostic information to help identify and troubleshoot the problem. Error output is typically displayed in the console or logged to a file for later analysis.


> In python         := print( )
>
> The print() function prints the specified message to the screen, or other standard output device. 
> The message can be a string, or any other object, the object will be converted into a string before being written to the screen.
>
> Syntax : print(object= separator= end= file= flush=)
>
> Here, details explanation of the above syntax :----
>
>> - object      :- Any object, and as many as you like. Will be converted to string before printed. 
>> - Sep         :- (optional) ; Specify how to separate the objects, if there is more than one, 
            the default is space '   '. 
>> - end         :- (optional) ;  Specify what to print at the end. Default is '\n' (line feed). 
>> - file        :- (optional) ;  where the values are printed. Its default value 
            is sys.stdout (screen).  
>> - flush       :- (optional) ; boolean specifying if the output is flushed or buffered,  
            the default: False. 
>
> The print() function, by default, adds a new-line at the end of the after printing message . 


> In c++            := cout << “message” << endl; 

> In javaScript     := console.log(“message”); 




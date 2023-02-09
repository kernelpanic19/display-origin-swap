' Initialize game variables
gameStatus = "In Progress"
gameType = "Request Selection"

' Initialize game
GameIntro()

' Game loop
While (gameStatus = "In Progress")      
    If (gameType = "Request Selection") Then
        GameSelect()
    EndIf
    InitializeGame()
    PlayGame()
    GameComplete()
EndWhile

' Game over
GameEnd()



Sub GameIntro
    TextWindow.WriteLine("Welcome To The Algebra Calculator Game!")
    TextWindow.WriteLine("What is your name?")
    name = TextWindow.Read()
    TextWindow.WriteLine("Hello " + name + "!")
EndSub

Sub GameSelect
    TextWindow.WriteLine("Choose Your Game by Entering a Number")
    TextWindow.WriteLine("[1] Addition 1-10")
    TextWindow.WriteLine("[2] Addition 1-100")
    TextWindow.WriteLine("[3] Subtraction 1-10")
    TextWindow.WriteLine("[4] Subtraction 1-100")
    gameSelection = TextWindow.Read()
    
    If (gameSelection = 1 or gameSelection = 3) Then
        maxNumber = 10
    Else
        maxNumber = 100
    EndIf

    If (gameSelection = 1 or gameSelection = 2) Then
        gameType = "Addition"
    Else
        gameType = "Subtraction"
    EndIf

    TextWindow.WriteLine("Great Choice " + name)

EndSub

Sub InitializeGame
    TextWindow.Clear()
    number1 = Math.GetRandomNumber(maxNumber)
    If (gameType = "Addition") Then
        ' Select result such that it is >= than number1
        equationResult = Math.GetRandomNumber(maxNumber - number1) + number1
        x = equationResult - number1
        TextWindow.WriteLine(number1 + " + x = " + equationResult)
    ElseIf (gameType = "Subtraction") Then
        ' Select result such that it is <= than number 1
        equationResult = Math.GetRandomNumber(number1)
        x = number1 - equationResult
        TextWindow.WriteLine(number1 + " - x = " + equationResult)
    EndIf
    TextWindow.WriteLine("x = " + x)
EndSub

Sub PlayGame
    correctGuess = "False"
    While correctGuess = "False"
        TextWindow.WriteLine("Please Enter The Value For X")
        guess = TextWindow.Read()
        If (guess = x) Then
            TextWindow.WriteLine("Correct!")
            correctGuess = "True"
        Else
            TextWindow.WriteLine("That Is Incorrect. Please Try Again.")
        EndIf
    EndWhile
EndSub
    

Sub GameComplete
    TextWindow.WriteLine("You You Like To:")
    TextWindow.WriteLine("[1] Continue")
    TextWindow.WriteLine("[2] Select a Different Game Type")
    TextWindow.WriteLine("[3] Quit?")
    replayChoice = TextWindow.Read()
    If (replayChoice = 2) Then
        gameType = "Request Selection"
    ElseIf (replayChoice = 3) Then
        gameStatus = "Game Over"
    EndIf
EndSub


Sub GameEnd
    TextWindow.WriteLine("Thanks for playing " + name + "!")
EndSub
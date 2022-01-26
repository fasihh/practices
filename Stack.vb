Module Module1
    Dim topOfStack As Integer = 9
    Dim bottomOfStack As Integer = 0
    Dim Stack(9) As String
    Dim StackPtr As Integer = 0


    Sub Main()
        Dim choice As Integer

        Do While choice > 4 Or choice < 1
            Console.WriteLine("Please enter your option: ")
            Console.WriteLine("1. Pop")
            Console.WriteLine("2. Push")

            choice = Console.ReadLine()

            If choice = 1 Then
                Call Pop()
                Call Main()
            End If
            If choice = 2 Then
                Call Push()
                Call Main()
            End If
        Loop

    End Sub

    Sub Pop()
        If StackPtr = bottomOfStack Then
            Console.WriteLine("Underflow")
        Else
            StackPtr = StackPtr - 1
            Console.WriteLine(Stack(1))
        End If

    End Sub
    Sub Push()
        Dim newVal As String
        Console.Write("Enter New Value: ")
        newVal = Console.ReadLine
        If StackPtr > topOfStack Then
            Console.WriteLine("Overflow")
        End If
        Stack(StackPtr) = newVal
        StackPtr = StackPtr + 1
    End Sub
End Module

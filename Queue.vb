Module Module1
    Dim FrontPointer As Integer
    Dim BackPointer As Integer
    Dim Queue(9) As String

    Sub Main()
        Dim choice As Integer

        Do While choice <= 4 Or choice >= 1
            Console.Write("Input choice: ")
            choice = Console.ReadLine

            If choice = 1 Then
                Add()
                Main()
            ElseIf choice = 2 Then
                Delete()
                Main()
            ElseIf choice = 3 Then
                For index = BackPointer To (FrontPointer - 1)
                    Console.WriteLine(Queue(index))
                Next
            End If
        Loop

    End Sub
    Sub Add()
        If FrontPointer = 10 Then
            Console.WriteLine("Overflow")
            Exit Sub
        End If
        Dim data As String
        Console.Write("Input data to be added: ")
        data = Console.ReadLine()
        Queue(FrontPointer) = data
        FrontPointer = FrontPointer + 1
    End Sub
    Sub Delete()
        If BackPointer = FrontPointer Then
            Console.WriteLine("Underflow")
            Exit Sub
        End If
        Dim data As String
        data = Queue(BackPointer)
        BackPointer = BackPointer + 1
    End Sub
End Module

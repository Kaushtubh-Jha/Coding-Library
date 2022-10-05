# Check givin number is Palindrome or not

Function Judge_Palindrome($arr)
{
    # Starting point is index -1 (the last character of the string) 
    # I am moving backwards towards the first character
    # Here I am just using a negative index greater than the string length -200
    $mem = $arr[-1..-200] -join '' 
    if ($arr -eq $mem) {
        return 1
    }
    return -1
}

FUnction Main{

    $array = 'KoloK'
    $result = Judge_Palindrome($array)
    if ($result -eq 1) {
        Write-Host "It's a Palindrome"
    }else {
        Write-Host "Not a Palindrome"
    }
}

Main

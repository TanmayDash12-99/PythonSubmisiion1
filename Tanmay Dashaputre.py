
NO_OF_CHARS = 256


# Find maximum distinct characters in  the string
def max_distinct_char(str, n):
    #print("My function is called ")
    # Initialize all character's
    # count with 0
    count = [0] * NO_OF_CHARS

    # Increase the count in array
    # if a character is found
    for i in range(n):
        #print("in loop ",i," looping ", ord(str[i]),"String value ", str[i])
        count[ord(str[i])] += 1

    max_distinct = 0
    for i in range(NO_OF_CHARS):
        if (count[i] != 0):
            max_distinct += 1

    return max_distinct


def getSmallesteSubstr(input_string):
    n = len(input_string)  # size of given string
    # Find maximum distinct characters
    # in any string
    max_distinct = max_distinct_char(input_string, n)
    return max_distinct


# Main Execution
if __name__ == "__main__":
    # Input String sample
    input_string = "abcda"

    Result_length = getSmallesteSubstr(input_string);
    print("Length of unique string ",Result_length)

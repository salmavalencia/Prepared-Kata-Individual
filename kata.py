def VariablesCount(booleanExpression):
    input_split = booleanExpression.split()
    characters_input = []

    for i in input_split:
        if any(c.isalpha() for c in i):
            if i[0] == "!":
                x = i.replace("!", "")
                if x not in characters_input:
                    characters_input.append(x)
            else:
                if i not in characters_input:
                    characters_input.append(i)
    
    return len(characters_input)


VariablesCount("a || b && !c || !b")
true.if = function (trueBlock, falseBlock) {
    return trueBlock()
}

true.ifTrue = function (trueBlock) {
    return trueBlock()
}

true.ifFalse = function (falseBlock) {
    return null
}


false.if = function (trueBlock, falseBlock) {
    return falseBlock()
}

false.ifTrue = function (trueBlock) {
    return null
}

false.ifFalse = function (falseBlock) {
    return falseBlock()
}

a = 5
b = (a < 5)
b.if(() => "true".print(), () => "false".print() )


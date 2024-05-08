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

trueBlock = () => "true".print()
falseBlock = () => "false".print()
a = 0;
(a < 5).if(trueBlock, falseBlock)
a = 10;
(a < 5).if(trueBlock, falseBlock)

